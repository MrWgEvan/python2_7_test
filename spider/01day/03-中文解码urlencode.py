# coding:utf-8
import urllib
import urllib2

def main():
    # 设置请求头
    req_headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
    }
    """编码工作使用urllib的urlencode()函数，帮我们将key:value这样的键值对转换成"key=value"这样的字符串，
    解码工作可以使用urllib的unquote()函数。（注意，不是urllib2.urlencode() )"""

    keyword = raw_input("请输入要查询的内容：")

    #只支持字典格式
    word = {"wd" : keyword,
            "ie":"utf-8"
            }

    #将中文转码
    wd = urllib.urlencode(word)
    print (wd)

    # 设置baidu查询请求信息
    url = "http://www.baidu.com/s?" + wd

    request = urllib2.Request(url, headers=req_headers)

    # 获取响应的内容
    response = urllib2.urlopen(request)
    # 读取出来
    html_Reader = response.read()

    file_write = open("baidu查询.html".decode("utf-8"), "wb")
    try:
        file_write.write(html_Reader)
    except Exception as exc:
        print (exc)
    finally:
        file_write.close()


if __name__ == "__main__":
    main()
