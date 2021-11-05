# bsc_trade_history

清晰展示币安智能链的交易历史

![vue](https://img.shields.io/badge/vue-v2.6.14-blue)
![vue-cli](https://img.shields.io/badge/vue--cli-v4.5.14-blue)
![node](https://img.shields.io/badge/node-v14.18.1-blue)
![npm](https://img.shields.io/badge/npm--cli-v6.14.15-blue)
![bootstrap](https://img.shields.io/badge/bootstrap-v5.1.3-green)
![bootstrap-vue](https://img.shields.io/badge/bootstrap--vue-2.21.2-green)
![Flask](https://img.shields.io/badge/Flask-v2.0.2-orange)
![python](https://img.shields.io/badge/python-v3.7.10-orange)

---

## 项目背景:

感觉[debank](https://debank.com/) 的交易历史功能不错，做个小项目练手。

Blog:[Crypto-BscTradeHistory Project](https://jerrychan807.github.io/2021/11/04/Crypto-BscTradeHistory%20Project/)

## 在线Demo:

[BscTradeHistory Website](http://app.foolisheddy.top:8080/history)

## 效果图:

![20211104132655](https://raw.githubusercontent.com/jerrychan807/imggg/master/image/20211104132655.png)

## 项目安装-Web

```bash
# 安装
npm install -g @vue/cli
npm install axios --save
npm install bootstrap --save
npm install bootstrap-vue --save
# 进入项目目录
cd client
# 运行Web
npm run serve
```

## 项目安装-Api

```bash
# 进入项目目录
cd server
# 安装pyproject.toml文件中的全部依赖
poetry install
# 配置bscscan apikey
vim config.py
# 运行api
poetry run python app.py
```

## Usage

访问 `http://YourIp:8080/history`