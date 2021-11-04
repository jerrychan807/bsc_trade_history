#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/3 4:12 PM
# @Author  : Jerry
# @Desc    : 
# @File    : parse_receipt_slave.py

import time
import json
import datetime
from pathlib import Path
from decimal import Decimal
from web3 import Web3

from bsc import Bsc, get_bnb_price, get_bsc_token_logo
from four_byte import get_function_name
from log import logger


class ParseReceiptSlave():
    def __init__(self, wallet_address):
        self.wallet_addr = Web3.toChecksumAddress(wallet_address)
        self.bsc_ins = Bsc()
        # self.transaction_info_list = []

    def parse_transaction_receipt(self, transaction_hash, token_address=''):
        all_token_transfered_dict = {"hash": transaction_hash, "token_transfered_list": []}
        try:
            receipt = self.bsc_ins.w3.eth.get_transaction_receipt(transaction_hash)
        except Exception as e:
            logger.error(e)
        else:
            logger.debug("receipt:{}".format(receipt))

            logs = self.bsc_ins.get_token_contract(token_address=token_address).events.Transfer().processReceipt(receipt)

            logger.debug("Transfer log length:{}".format(len(logs)))
            for log in logs:
                # amount = Decimal(self.w3.fromWei(log["args"]["value"], 'ether'))
                # Transfer event要和地址相关联
                if log["args"]["from"] == self.wallet_addr or log["args"]["to"] == self.wallet_addr:
                    token_address = log["address"]
                    token_symbol = self.bsc_ins.get_token_symbol(token_address)
                    _amount = Decimal(log["args"]["value"] / Decimal(10 ** self.bsc_ins.get_token_decimals(
                        token_address=token_address)))
                    side = "reduce" if log["args"]["from"] == self.wallet_addr else "add"
                    amount = _amount.quantize(Decimal("0.00"))  # 保留两位小数
                    token_transfered_dict = {"token_symbol": token_symbol, "amount": str(amount), "side": side}

                    image_url = get_bsc_token_logo(token_address)
                    token_transfered_dict["image_url"] = image_url if image_url else ""
                    # print(token_transfered_dict)

                    all_token_transfered_dict["token_transfered_list"].append(token_transfered_dict)
        return all_token_transfered_dict


def parse_receipt_slave(wallet_address, transaction_hash, contract_address):
    slave = ParseReceiptSlave(wallet_address)
    all_token_transfered_dict = slave.parse_transaction_receipt(transaction_hash, contract_address)
    return all_token_transfered_dict


if __name__ == '__main__':
    wallet_address = "0x91f24dC6feed1461B5A17360bf118C5c21147939"
    transaction_hash = "0x5863726b65bba2f578e728dc9308cce07510d0c30813a68e1a0015c0d8e07d90"
    contract_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
    parse_receipt_slave(wallet_address, transaction_hash, contract_address)
