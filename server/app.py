#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2021/10/26 5:07 PM
# @Author  : Jerry
# @Desc    : 
# @File    : app.py

from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request
from history_parser import query_bsc_history
import json
from demo_data import transaction_info_list

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

RESOURCES = [
    {
        'sn': 'SSNI-103',
        'teacher': '葵つかさ',
        'learnt': True
    },
    {
        'sn': 'JUY-349',
        'teacher': '蒂亚',
        'learnt': False
    },
    {
        'sn': 'MXSPS-535',
        'teacher': '麻生希',
        'learnt': True
    }
]


# sanity check route
@app.route('/open', methods=['GET'])
def open_door():
    return jsonify(u'芝麻开门！')


@app.route('/resources', methods=['GET', 'POST'])
def all_res():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        RESOURCES.append({
            'sn': post_data.get('sn'),
            'teacher': post_data.get('teacher'),
            'learnt': post_data.get('learnt')
        })
        response_object['message'] = '资源添加成功！'
    else:
        response_object['resources'] = RESOURCES
    return jsonify(response_object)


@app.route('/history', methods=['POST'])
def history():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        transaction_info_list = query_bsc_history(post_data.get('address'), int(post_data.get('page')),
                                                  int(post_data.get('offset')))
        response_object['result'] = transaction_info_list
    return jsonify(response_object)


@app.route('/historyDemo', methods=['POST'])
def history_demo():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        response_object['result'] = transaction_info_list
    return jsonify(response_object)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host="0.0.0.0")
