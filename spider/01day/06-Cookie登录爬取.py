# coding:utf-8

import urllib2
# 1. 导入Python SSL处理模块
import ssl


def main():

    url = "https://python.freelycode.com/user/home"

    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()

    header = {
        "Host": " python.freelycode.com",
        "Connection": " keep-alive",
        "Cache-Control": " max-age=0",
        #"Upgrade-Insecure-Requests": " 1",
        "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://python.freelycode.com/accounts/login/",
        #"Accept-Encoding": " gzip, deflate, sdch, br",
        "Accept-Language": " zh-CN,zh;q=0.8",
        "Cookie": " UM_distinctid=1604b2a95d35e4-01154e8cc7dc2a-6b1b1279-100200-1604b2a95d443b; CNZZDATA1255270602=1409519339-1513088273-%7C1513088273; csrftoken=9dGjkOhghpiTC3aCGBTiFdXMfBjznlCQ; sessionid=ode270lt0l65hiv32vd9q3plmchpx3nk"

    }

    request = urllib2.Request(url,headers=header)

    response = urllib2.urlopen(request,context=context)

    with open("cookie.html","w") as f:
        f.write(response.read())


if __name__ == '__main__':
        main()