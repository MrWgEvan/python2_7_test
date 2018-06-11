# coding:utf-8
import urllib2
import random

def main():
    # 设置请求头
    req_headers = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"
    ]

    # url = "http://www.163.com/"
    url = "http://blog.csdn.net/ying890/article/details/25541169/"

    # 从list中选取一个
    user_Agent = random.choice(req_headers)
    # 设置请求信息
    request = urllib2.Request(url)

    # 将user-agent添加到报头中
    request.add_header("User-Agent",user_Agent)
    #只能首字母大写
    print request.get_header("User-agent")
    # 获取响应的内容
    response = urllib2.urlopen(request)

    # 读取出来
    html_Reader = response.read()

    file_write = open("bushu2.html", "wb")
    try:
        file_write.write(html_Reader)
        print "ok"
    except Exception as exc:
        print (exc)
    finally:
        file_write.close()
        # file_reade.close()


if __name__ == "__main__":
    main()




