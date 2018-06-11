# coding:utf-8

import urllib2


def main():
    """
    基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
    使用相关的 Handler处理器 来创建特定功能的处理器对象；
    然后通过 urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
    使用自定义的opener对象，调用open()方法发送请求。
    """
    # 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
    #http_handler = urllib2.HTTPHandler()
    # https_handler = urllib2.HTTPSHandler()

    """如果在 HTTPHandler()增加 debuglevel=1参数，还会将 Debug Log 打开，这样程序在执行的时候，
    会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作"""
    http_handler = urllib2.HTTPHandler(debuglevel=1)

    # 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
    opener = urllib2.build_opener(http_handler)

    # 构建 Request请求
    url = "http://www.baidu.com/"
    request = urllib2.Request(url)

    # 调用自定义opener对象的open()方法，发送request请求
    response = opener.open(request)

    #print(response.read())


if __name__ == '__main__':
    main()
