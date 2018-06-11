# coding:utf-8

import urllib
import urllib2


def main():
    """
    请求的时候出现{"errorCode":50}。
    今天在某网里面看到有人说只要去除url里面translate_o的_o字段，就可以解决问题。
    """
    url= "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom= "

    headers = {
        "Host": "fanyi.youdao.com",
        "Connection": "keep-alive", # 是否保持连接
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Language": "zh-CN,zh;q=0.8"
        # "Content-Length": "230", 字符串长度
        # "Referer": "http://fanyi.youdao.com/", 重定向
        # "Origin": "http://fanyi.youdao.com",  Origin字段里只包含是谁发起的请求
        # "Accept-Encoding": "gzip, deflate", 转换为zip格式，不能选

    }
    key = raw_input("请输入要翻译的单词：")

    post_data = {
        "from": "AUTO",
        "i": key,
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        # "salt": "1512907513456",
        # "sign": "372831128f05775bfeafad2138b44fe8",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "true"
    }
    post_data = urllib.urlencode(post_data)
    print post_data

    request = urllib2.Request(url,data=post_data,headers=headers)
    response = urllib2.urlopen(request)

    print ("*"*30)
    print (response.read())


if __name__ == '__main__':
    main()
