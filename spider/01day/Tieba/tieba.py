# coding:utf-8
import urllib
import urllib2


def file_down(file_url):
    """
    发送请求信息
    返回页面数据
    """
    req_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " +
                      "Chrome/57.0.2987.110 Safari/537.36"
    }
    request = urllib2.Request(file_url, headers=req_headers)
    response = urllib2.urlopen(request)
    return response.read()


def file_write(file_read,i):
    """
    将页面保存到文件
    """
    filename = "第"+str(i)+"页.html"
    print ("正在保存"+filename)
    with open(filename.decode("utf-8"), "w") as f:
        f.write(file_read)


def file_find(ba_name, min_page, max_page):
    """
    管理数据
    """
    url = "http://tieba.baidu.com/f?"
    kw_1 = {"kw": ba_name}
    kw_2 = urllib.urlencode(kw_1)

    for i in range(int(min_page),int(max_page)+1):
        pn = (i - 1)*50
        fill_url = url + kw_2 + "&pn="+str(pn)
        print ("正在处理第%d页....."%i)
        file_read = file_down(fill_url)
        file_write(file_read, i)
        print ("-"*30)
    print ("下载完成。。。")


# 中央调度器
def main():
    # url = "http://tieba.baidu.com/f?"
    ba_name = raw_input("请输入要爬取的贴吧：")
    min_page = raw_input("请输入爬取开始的页面：")
    max_page = raw_input("请输入爬取截止的页面：")
    file_find(ba_name,min_page,max_page)


if __name__ == '__main__':
    main()
