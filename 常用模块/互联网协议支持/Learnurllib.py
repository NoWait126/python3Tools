# -*- coding: utf-8 -*-

import urllib
from urllib import request
'''
urllib 是一个收集了多个使用URL的模块的软件包：
  urllib.request 打开和阅读 URLs
  urllib.error 包含 urllib.request 抛出的异常
  urllib.parse 用于处理 URL
  urllib.robotparser 用于解析 robots.txt 文件
  
'''

# 可以直接用urlopen请求url
def openDirec(url):
    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

    # 也可以模拟浏览器请求
def imitateBroswer(url):
    req = request.Request(targetUrl)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


if __name__ == '__main__':
    targetUrl  = 'https://www.python.org/'
    imitateBroswer(targetUrl)