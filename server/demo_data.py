#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2021/11/2 4:16 PM
# @Author  : Jerry
# @Desc    : 
# @File    : 1.py

transaction_info_list = [{
            "contract_address": "0x55d398326f99059fF775485246999027B3197955",
            "cost_bnb": "0.0001",
            "cost_usd": "0.0571",
            "date": "2021-10-30 13:41:02",
            "func_name": "transfer",
            "logo_url": "https://debank.com/static/media/contract.13bef102.svg",
            "project_name": "Unknown",
            "token_transfered_list": [
                {
                    "amount": "32.25",
                    "image_url": "https://bscscan.com/token/images/busdt_32.png",
                    "side": "reduce",
                    "token_symbol": "USDT"
                }
            ]
        },
            {
                "contract_address": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
                "cost_bnb": "0.0009",
                "cost_usd": "0.4737",
                "date": "2021-10-30 13:38:35",
                "func_name": "swapExactTokensForTokens",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_pancakeswap/a4e035cf4495755fddd5ebb6e5657f63.png",
                "project_name": "PancakeSwap",
                "token_transfered_list": [
                    {
                        "amount": "4.98",
                        "image_url": "https://bscscan.com/images/main/empty-token.png",
                        "side": "reduce",
                        "token_symbol": "Guru"
                    },
                    {
                        "amount": "32.25",
                        "image_url": "https://bscscan.com/token/images/busdt_32.png",
                        "side": "add",
                        "token_symbol": "USDT"
                    }
                ]
            },
            {
                "contract_address": "0xAaD15F24f24c6a67b159e5ddb50376ce348Fb668",
                "cost_bnb": "0.0006",
                "cost_usd": "0.3376",
                "date": "2021-10-30 13:37:05",
                "func_name": "deposit",
                "logo_url": "https://debank.com/static/media/contract.13bef102.svg",
                "project_name": "Unknown",
                "token_transfered_list": [
                    {
                        "amount": "4.98",
                        "image_url": "https://bscscan.com/images/main/empty-token.png",
                        "side": "add",
                        "token_symbol": "Guru"
                    }
                ]
            },
            {
                "contract_address": "0x55d398326f99059fF775485246999027B3197955",
                "cost_bnb": "0.0001",
                "cost_usd": "0.0515",
                "date": "2021-10-25 11:42:12",
                "func_name": "transfer",
                "logo_url": "https://debank.com/static/media/contract.13bef102.svg",
                "project_name": "Unknown",
                "token_transfered_list": [
                    {
                        "amount": "488.90",
                        "image_url": "https://bscscan.com/token/images/busdt_32.png",
                        "side": "reduce",
                        "token_symbol": "USDT"
                    }
                ]
            },
            {
                "contract_address": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
                "cost_bnb": "0.0006",
                "cost_usd": "0.2999",
                "date": "2021-10-25 11:41:48",
                "func_name": "swapExactTokensForETH",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_pancakeswap/a4e035cf4495755fddd5ebb6e5657f63.png",
                "project_name": "PancakeSwap",
                "token_transfered_list": [
                    {
                        "amount": "10.00",
                        "image_url": "https://bscscan.com/token/images/busdt_32.png",
                        "side": "reduce",
                        "token_symbol": "USDT"
                    }
                ]
            },
            {
                "contract_address": "0xec3422Ef92B2fb59e84c8B02Ba73F1fE84Ed8D71",
                "cost_bnb": "0.0009",
                "cost_usd": "0.4366",
                "date": "2021-10-25 11:40:36",
                "func_name": "repayBorrow",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_venus/db05054f7f5306ff2f083a7860aafcb2.png",
                "project_name": "Venus",
                "token_transfered_list": [
                    {
                        "amount": "3.99",
                        "image_url": "https://bscscan.com/token/images/dogecoin_32.png",
                        "side": "reduce",
                        "token_symbol": "DOGE"
                    }
                ]
            },
            {
                "contract_address": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
                "cost_bnb": "0.0007",
                "cost_usd": "0.3349",
                "date": "2021-10-25 11:40:06",
                "func_name": "swapTokensForExactTokens",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_pancakeswap/a4e035cf4495755fddd5ebb6e5657f63.png",
                "project_name": "PancakeSwap",
                "token_transfered_list": [
                    {
                        "amount": "1.10",
                        "image_url": "https://bscscan.com/token/images/busdt_32.png",
                        "side": "reduce",
                        "token_symbol": "USDT"
                    },
                    {
                        "amount": "4.00",
                        "image_url": "https://bscscan.com/token/images/dogecoin_32.png",
                        "side": "add",
                        "token_symbol": "DOGE"
                    }
                ]
            },
            {
                "contract_address": "0xfD5840Cd36d94D7229439859C0112a4185BC0255",
                "cost_bnb": "0.0028",
                "cost_usd": "1.3246",
                "date": "2021-10-25 11:38:45",
                "func_name": "redeemUnderlying",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_venus/db05054f7f5306ff2f083a7860aafcb2.png",
                "project_name": "Venus",
                "token_transfered_list": [
                    {
                        "amount": "500.00",
                        "image_url": "https://bscscan.com/token/images/busdt_32.png",
                        "side": "add",
                        "token_symbol": "USDT"
                    },
                    {
                        "amount": "23610.05",
                        "image_url": "https://bscscan.com/token/images/venus-vusdt_32.png",
                        "side": "reduce",
                        "token_symbol": "vUSDT"
                    }
                ]
            },
            {
                "contract_address": "0xec3422Ef92B2fb59e84c8B02Ba73F1fE84Ed8D71",
                "cost_bnb": "0.0009",
                "cost_usd": "0.4358",
                "date": "2021-10-25 11:37:00",
                "func_name": "repayBorrow",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_venus/db05054f7f5306ff2f083a7860aafcb2.png",
                "project_name": "Venus",
                "token_transfered_list": [
                    {
                        "amount": "3335.20",
                        "image_url": "https://bscscan.com/token/images/dogecoin_32.png",
                        "side": "reduce",
                        "token_symbol": "DOGE"
                    }
                ]
            },
            {
                "contract_address": "0xec3422Ef92B2fb59e84c8B02Ba73F1fE84Ed8D71",
                "cost_bnb": "0.0029",
                "cost_usd": "1.4091",
                "date": "2021-10-25 11:36:06",
                "func_name": "redeem",
                "logo_url": "https://static.debank.com/image/project/logo_url/bsc_venus/db05054f7f5306ff2f083a7860aafcb2.png",
                "project_name": "Venus",
                "token_transfered_list": [
                    {
                        "amount": "3335.20",
                        "image_url": "https://bscscan.com/token/images/dogecoin_32.png",
                        "side": "add",
                        "token_symbol": "DOGE"
                    },
                    {
                        "amount": "166149.04",
                        "image_url": "https://bscscan.com/token/images/venus-doge_32.png?=v1",
                        "side": "reduce",
                        "token_symbol": "vDOGE"
                    }
                ]

            }
        ]