# coding:utf-8

import urllib2


def main():

    # 定义一个代理开关
    proxy_switch = True

    # 构建了两个代理Handler，一个有代理IP，一个没有代理IP
    proxy_headler = urllib2.ProxyHandler({"http":"101.81.105.233:9000"})
    null_headler  = urllib2.ProxyHandler({})

    if proxy_switch:
        opener = urllib2.build_opener(proxy_headler)
    else:
        opener = urllib2.build_opener(null_headler)

    request = urllib2.Request("http://www.baidu.com/")

    # 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
    response = opener.open(request)

    # 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
    # urllib2.install_opener(opener)
    # response = urlopen(request)


    # 有时候会使用decode("utf-8")来解码
    print (response.read())


if __name__ == '__main__':
    main()
