# 码市爬虫项目

> 无聊打开码市抓包看到他的接口挺好搞的，随手写个爬虫。。。

## 项目思路

1. 通过爬虫爬取码市项目信息，并存储到mongodb
2. 定时监测数据库项目数据，看过了的标记`like`为`true`，监测到新项目并且项目介绍符合关键字则发邮件

## 项目实现

- 使用 `aiohttp` 写异步爬虫
- 邮件方面用了第三方库 `yagmail` 便捷一点
- 使用 `APscheduler`做任务定时器，设定一小时爬一次

## 项目安装

```bash
git clone https://github.com/feng409/codemart-spider.git
cd codemart-spider
pip install -r requirements.txt
cp config.py.example config.py
vim config.py
python run.py
```

## 环境要求

- Python3.6及以上