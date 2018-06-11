# -*- coding:utf-8 -*-

import requests

def request_demo1():
    url_test = "http://www.baidu.com/s?"
    params = {"ie":"utf-8","wd":"哈哈"}
    response = requests.get(url_test,params=params)
    # 响应首部
    print response.headers
    # 状态码
    print response.status_code
    # 原因短语
    print response.reason
    #print response.json() 返回的是json数据

    # 响应内容
    #print response.content
    # 内容文本
    #print response.text

    print response.url

if __name__ == '__main__':
    request_demo1()