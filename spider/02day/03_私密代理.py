import urllib2

import os

def main():

    """
    可以将帐号密码设置到系统环境变量中，避免泄露
    user = os.environ.get("user")
    pwd = os.environ.get("pwd")
    """

    hand_clq = urllib2.ProxyHandler({"http" : "帐号:密码@101.81.105.233:端口号" })

    opener = urllib2.build_opener(hand_clq)

    request = urllib2.Request("http://www.baidu.com/")

    response = opener.open(request)

    response.read()

if __name__ == '__main__':
    main()