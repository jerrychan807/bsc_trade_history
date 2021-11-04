#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2021/10/27 4:43 PM
# @Author  : Jerry
# @Desc    : 
# @File    : history_parser.py
import multiprocessing
import time
import json
import datetime
import queue
from pathlib import Path
from decimal import Decimal
from web3 import Web3

from bsc import Bsc, get_bnb_price, get_bsc_token_logo

from log import logger

from parse_receipt_slave import parse_receipt_slave


class HistoryParser():
    def __init__(self, wallet_address, page, offset):
        self.wallet_addr = Web3.toChecksumAddress(wallet_address)
        self.bsc_ins = Bsc()
        self.page = page
        self.offset = offset
        self.transaction_info_list = []
        self.task_queue = queue.Queue()

    def read_known_contract(self):
        with Path('known_contract.json').open('r') as f:
            self.known_contract_dict = json.load(f)

    def query_contract_related_project_info(self, contract_address):
        for project_name, info_dict in self.known_contract_dict.items():
            if contract_address in info_dict["contract_list"]:
                return project_name, info_dict["logo_url"]
        return "Unknown", self.known_contract_dict["Unknown"]["logo_url"]

    def parse_transaction(self, hash_info):
        logger.debug("parse transaction. hash:{}".format(hash_info["hash"]))
        transaction_info = {}
        transaction_info["hash"] = hash_info["hash"]
        transaction_info["date"] = timestamp2date(int(hash_info["timeStamp"]))
        contract_address = Web3.toChecksumAddress(hash_info["to"])
        if_contract_flag = self.bsc_ins.check_if_contract(contract_address)
        logger.debug("contract_address. if_contract_flag:{}".format(if_contract_flag))
        if if_contract_flag:
            input_data = hash_info["input"]
            four_byte = input_data[0:10]
            gas_fee_amount_bnb = Decimal(self.bsc_ins.w3.fromWei(int(hash_info["gasPrice"]) * int(hash_info["gasUsed"]),
                                                                 'ether'))
            coingecko_date_str = get_coingecko_datestr(transaction_info["date"])
            current_bnb_price_usd = get_bnb_price(coingecko_date_str)
            gas_fee_cost_usd = Decimal(Decimal(current_bnb_price_usd) * gas_fee_amount_bnb).quantize(Decimal("0.0000"))
            gas_fee_amount_bnb_decimal4 = gas_fee_amount_bnb.quantize(Decimal("0.0000"))
            transaction_info["cost_bnb"] = str(gas_fee_amount_bnb_decimal4)  # gas fee花费的bnb数量
            transaction_info["cost_usd"] = str(gas_fee_cost_usd)  # gas fee花费的usd

            func_name = self.bsc_ins.get_transaction_function_name(contract_address, four_byte, input_data)
            # if not if_contract_flag:
            #     func_name = "Transfer"
            logger.debug("func_name: {}".format(func_name))

            transaction_info["contract_address"] = contract_address
            transaction_info["func_name"] = func_name  # 调用函数名
            transaction_info["project_name"], transaction_info["logo_url"] = self.query_contract_related_project_info(
                contract_address)
            logger.debug("parse transaction receipt. hash:{}".format(hash_info["hash"]))

            self.task_queue.put((self.wallet_addr, hash_info["hash"], contract_address))
            # transaction_info["token_transfered_list"] = self.parse_transaction_receipt(transaction_hash=hash_info["hash"],
            #                                                                            token_address=contract_address)
            self.transaction_info_list.append(transaction_info)

    def run_parse_transaction_receipt(self):
        result_list = []
        logger.debug("task_queue length:{}".format(self.task_queue.qsize()))
        if self.task_queue.qsize():  # 避免queue size为0,频繁创建进程池
            try:
                pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
                while not self.task_queue.empty():  # 使用empty()判断队列是否为空
                    item = self.task_queue.get()
                    # item value is tuple(region, hostname, logset_id, logset_name）
                    # result_list.append(pool.apply_async(self.parse_transaction_receipt, (item[0], item[1])))
                    result_list.append(pool.apply_async(parse_receipt_slave, (item[0], item[1], item[2])))
                pool.close()
                pool.join()
            except Exception as e:
                print(e)

        if result_list:
            for r in result_list:
                all_token_transfered_dict = r.get()
                for transaction_info_dict in self.transaction_info_list:
                    if transaction_info_dict["hash"] == all_token_transfered_dict["hash"]:
                        transaction_info_dict["token_transfered_list"] = all_token_transfered_dict[
                            "token_transfered_list"]

    # def parse_transaction_receipt(self, transaction_hash, token_address=''):
    #     receipt = self.bsc_ins.w3.eth.get_transaction_receipt(transaction_hash)
    #     logger.debug("receipt:{}".format(receipt))
    #
    #     logs = self.bsc_ins.get_token_contract(token_address=token_address).events.Transfer().processReceipt(receipt)
    #     token_transfered_list = []
    #     logger.debug("Transfer log length:{}".format(len(logs)))
    #     for log in logs:
    #         # amount = Decimal(self.w3.fromWei(log["args"]["value"], 'ether'))
    #         # Transfer event要和地址相关联
    #         if log["args"]["from"] == self.wallet_addr or log["args"]["to"] == self.wallet_addr:
    #             token_address = log["address"]
    #             token_symbol = self.bsc_ins.get_token_symbol(token_address)
    #             _amount = Decimal(log["args"]["value"] / Decimal(10 ** self.bsc_ins.get_token_decimals(
    #                 token_address=token_address)))
    #             side = "reduce" if log["args"]["from"] == self.wallet_addr else "add"
    #             amount = _amount.quantize(Decimal("0.00"))  # 保留两位小数
    #             token_transfered_dict = {"token_symbol": token_symbol, "amount": str(amount), "side": side}
    #
    #             image_url = get_bsc_token_logo(token_address)
    #             token_transfered_dict["image_url"] = image_url if image_url else ""
    #             # print(token_transfered_dict)
    #
    #             token_transfered_list.append(token_transfered_dict)
    #     return token_transfered_list


def timestamp2date(timestamp):
    time_array = time.localtime(timestamp)
    date_str = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return date_str


def get_coingecko_datestr(date_str):
    d1 = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    return "{}-{}-{}".format(d1.day, d1.month, d1.year)


def query_bsc_history(address, page, offset):
    history = HistoryParser(wallet_address=address, page=page, offset=offset)
    history.read_known_contract()
    logger.debug("start to get_normal_transactions_list")
    hash_info_list = history.bsc_ins.get_normal_transactions_list(history.wallet_addr, page, offset)
    logger.debug("hash_info_list length: {}".format(len(hash_info_list)))
    num = 0
    for hash_info in hash_info_list:
        num += 1
        history.parse_transaction(hash_info)
        # print('==========')
        # if num > 3:
        #     break
    history.run_parse_transaction_receipt()
    # for each in history.transaction_info_list:
    #     print(each)
    return history.transaction_info_list


if __name__ == '__main__':
    address = "0x6bf1d2B66Ae5Fd6bB31A56EF22f3d4c9D1340Aa7"
    page = 3
    offset = 10
    res = query_bsc_history(address, page, offset)
    print(res)
