# bsc_trade_history

Make your BSC transaction simple. 

![vue](https://img.shields.io/badge/vue-v2.6.14-blue)
![vue-cli](https://img.shields.io/badge/vue--cli-v4.5.14-blue)
![node](https://img.shields.io/badge/node-v14.18.1-blue)
![npm](https://img.shields.io/badge/npm--cli-v6.14.15-blue)
![bootstrap](https://img.shields.io/badge/bootstrap-v5.1.3-green)
![bootstrap-vue](https://img.shields.io/badge/bootstrap--vue-2.21.2-green)
![Flask](https://img.shields.io/badge/Flask-v2.0.2-orange)
![python](https://img.shields.io/badge/python-v3.7.10-orange)

[中文ReadMe](https://github.com/jerrychan807/bsc_trade_history/blob/main/READMEcn.md)

---

## Background:

inspired by [debank](https://debank.com/) ,Practice my hands on this small project

Blog:[Crypto-BscTradeHistory Project](https://jerrychan807.github.io/2021/11/04/Crypto-BscTradeHistory%20Project/)

## Online Demo:

[BscTradeHistory Website](https://bsc-trade-history.vercel.app/history)

## Snapshot:

![20211104132655](https://raw.githubusercontent.com/jerrychan807/imggg/master/image/20211104132655.png)

## Install-Web

```bash
# install
npm install -g @vue/cli
npm install axios --save
npm install bootstrap --save
npm install bootstrap-vue --save
# enter web project directory
cd client
# run Web
npm run serve
```

## Install-Api

```bash
# enter web project directory
cd server
# install pyproject.toml required package
poetry install
# enter your bscscan apikey
vim config.py
# run Api
poetry run python app.py
```

## Usage

visit `http://YourIp:8080/history`