#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2021/10/28 5:36 PM
# @Author  : Jerry
# @Desc    : 
# @File    : bsc.py


from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.types import BlockIdentifier, ChecksumAddress, HexBytes, Nonce, TxParams, TxReceipt, Wei
from web3.contract import Contract, ContractFunction

from decimal import Decimal
from pathlib import Path
import requests
from four_byte import get_function_name
from pycoingecko import CoinGeckoAPI
from bs4 import BeautifulSoup as bs

from config import RPC, BscScanApiKey


class Bsc():
    def __init__(self):
        w3_provider = Web3.HTTPProvider(endpoint_uri=RPC)
        self.w3 = Web3(provider=w3_provider)
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)  # 注入poa中间件

    def get_latest_blocknum(self):
        block = self.w3.eth.get_block('latest')
        return int(block['number'])

    def get_contract_abi_json(self, contract_address):
        bsc_api_url = "https://api.bscscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={YourApiKeyToken}".format(
            contract_address=contract_address, YourApiKeyToken=BscScanApiKey)
        res = requests.get(bsc_api_url, timeout=10)
        res_json = res.json()
        contract_abi_json = res_json["result"]
        return contract_abi_json

    def get_normal_transactions_list(self, wallet_addr, page, offset):
        current_blocknumber = self.get_latest_blocknum()
        startblock = current_blocknumber - (30000 * 30)
        bsc_api_url = "https://api.bscscan.com/api?module=account&action=txlist&address={address}&startblock={startblock}&endblock={endblock}&page={page}&offset={offset}&sort=desc&apikey={YourApiKeyToken}".format(
            address=wallet_addr, startblock=startblock, endblock=current_blocknumber, page=page, offset=offset,
            YourApiKeyToken=BscScanApiKey)
        print(bsc_api_url)
        res = requests.get(bsc_api_url, timeout=10)
        res_json = res.json()
        # print(res_json)

        hash_info_list = []
        if res_json:
            hash_info_list = [trans for trans in res_json["result"]]
        return hash_info_list

    def get_token_contract(self, token_address: ChecksumAddress) -> Contract:
        """获取token合约对象

        :param token_address:
        :return:
        """
        with Path('abi/bep20.abi').open('r') as f:
            abi = f.read()
        return self.w3.eth.contract(address=token_address, abi=abi)

    def get_token_decimals(self, token_address: ChecksumAddress) -> int:
        """获取token小数点位数

        :param token_address:
        :return:
        """
        token_contract = self.get_token_contract(token_address=token_address)
        decimals = token_contract.functions.decimals().call()
        return int(decimals)

    def get_token_symbol(self, token_address: ChecksumAddress) -> str:
        token_contract = self.get_token_contract(token_address=token_address)
        symbol = token_contract.functions.symbol().call()
        return symbol

    def get_token_contract_with_abi(self, contract_address, abi):
        return self.w3.eth.contract(address=contract_address, abi=abi)

    def check_if_contract(self, contract_address):
        bytecode = self.w3.eth.get_code(contract_address)
        if len(bytecode) > 1:
            return True
        else:
            return False

    def get_transaction_function_name(self, contract_address, four_byte, input_data):
        contract_abi_json = self.get_contract_abi_json(contract_address)
        if contract_abi_json == "Contract source code not verified":
            func_name = get_function_name(four_byte)
        else:
            contract_ins = self.get_token_contract_with_abi(contract_address, contract_abi_json)
            try:
                func, params = contract_ins.decode_function_input(input_data)
            except ValueError:
                func_name = get_function_name(four_byte)
            else:
                func_name = func.fn_name
        return func_name


def get_bnb_price(date_str):
    """
    调取CoinGeckoAPI获取历史bnb价格
    :param date_str: 日期 "dd-mm-yyyy"
    :return:
    """
    cg = CoinGeckoAPI()
    res = cg.get_coin_history_by_id(id='binancecoin', vs_currency='usd', date=date_str)
    date_price = Decimal(res["market_data"]["current_price"]["usd"]).quantize(Decimal("0.00"))
    return date_price


def get_bsc_token_logo(token_address):
    try:
        header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', }
        res = requests.get(url="https://bscscan.com/address/{}".format(token_address), headers=header,
                           timeout=10)

        soup = bs(res.text, 'html.parser')
        images = soup.find('div', attrs={'id': 'ContentPlaceHolder1_tr_tokeninfo'}).findAll('img')
        image_full_url = "https://bscscan.com{}".format(images[0]['src'])
    except:
        return None
    return image_full_url


if __name__ == '__main__':
    # price = get_bnb_price(date_str="25-10-2021")
    # print(price)
    bsc = Bsc()
    # res = bsc.get_latest_blocknum()
    # print(res)
    res = bsc.check_if_contract(contract_address="0x302c98e6d6A65Bf15255b81972f9EaA1F45438C8")
    print(res)
    res = bsc.check_if_contract(contract_address="0x3B0969c3F03Bc0ab35ff9B8784904de6c381250A")
    print(res)
    # get_bsc_token_logo()
