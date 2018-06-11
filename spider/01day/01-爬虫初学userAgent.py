# coding:utf-8
import urllib2

def main():
    # 设置请求头
    req_headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
    }
    # 设置请求信息
    request = urllib2.Request("http://www.baidu.com/", headers=req_headers)

    # 获取响应的内容
    response = urllib2.urlopen(request)
    # 读取出来
    html_Reader = response.read()

    '''print (html_Reader.decode("utf-8"))
        file_reade = file(html_Reader, "r")'''
    file_write = open("baidu.html", "wb")
    try:
        """
        while True:
            block = file_reade.read(1024)
            if not block:
                break
        """
        file_write.write(html_Reader)
    except Exception as exc:
        print (exc)
    finally:
        file_write.close()
        # file_reade.close()


if __name__ == "__main__":
    main()




