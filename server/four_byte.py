#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2021/10/28 2:02 PM
# @Author  : Jerry
# @Desc    : 
# @File    : 4byte.py

""" 4byte.directory API
Ref: https://www.4byte.directory/docs/
"""
import requests


def url(endpoint):
    return 'https://www.4byte.directory/api/v1/{}/'.format(endpoint)


def get(endpoint, page=0, params={}):
    params['page'] = page
    # TODO: will probably want to be more defensive and add error handling
    return requests.get(url(endpoint), params=params).json()


def get_all(endpoint, params):
    page = 1
    results = []

    while True:
        res = get(endpoint, page, params)
        next_url = res.get('next')
        results.extend(res.get('results', []))

        if not next_url:
            break

        page += 1

    return results


def signatures(**kwargs):
    """
    Get signatures
    kwargs
    ======
    text_signature
    text_signature__iexact
    text_signature__contains
    text_signature__icontains
    text_signature__startswith
    text_signature__istartswith
    text_signature__endswith
    text_signature__iendswith
    hex_signature
    """
    # If we're given an ID we're getting a specific signature
    if kwargs.get('id'):
        return get('signatures/{}'.format(kwargs['id']))

    return get_all('signatures', params=kwargs)


def get_function_name(hex_signature):
    result = signatures(hex_signature=hex_signature)
    function_name = 'unknown'
    if result:
        text_signature = result[0]["text_signature"]
        function_name = text_signature.split("(")[0]
    return function_name


if __name__ == '__main__':
    test_dict = {
        "id": 1,
        "hex_signature": "0x722713f7",
    }
    result = signatures(hex_signature="0xb6b55f25")
    print(result)
    # [{'id': 894, 'created_at': '2016-07-09T05:56:01.468494Z', 'text_signature': 'deposit(uint256)', 'hex_signature': '0xb6b55f25', 'bytes_signature': '¶µ_%'}]

    text_signature = result[0]["text_signature"]
    function_name = text_signature.split("(")[0]
    print(function_name)