# coding:utf-8

import urllib2
import urllib
import cookielib


def main():

    # 获取一个CookieJar
    cookie = cookielib.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(cookie_handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    opener.addheaders = [("User-Agent"," Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]

    data = {"username":"","password":""}

    data = urllib.urlencode(data)

    request = urllib2.Request("http://python.freelycode.com/accounts/login/",data=data)

    opener.open(request)

    # 这个网址没办法这样登陆保存cookie，得到的cookie是错误的是错误的
    for item in cookie:
        print (item.name+"　：　"+item.value)

    response2 = opener.open("http://python.freelycode.com/user/home/")
    # print (response2.read())
    with open("Python部落.html".decode("utf-8"), "w") as f:
        f.write(response2.read())
    print ("111111")


if __name__ == '__main__':
    main()

