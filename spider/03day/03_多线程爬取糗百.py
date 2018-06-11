# -*- coding:utf-8 -*-

import threading
from Queue import Queue
import requests
from bs4 import BeautifulSoup
import re,json,os,time

#两个队列标识符
PAGE_EXIT = False
PARSE_EXIT = False

# 爬取线程
class spiderThread(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        # 调用父类初始化方法
        super(spiderThread,self).__init__()
        # 线程名
        self.threadName = threadName
        # 爬取页码队列
        self.pageQueue = pageQueue
        # 爬取到的数据队列
        self.dataQueue = dataQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36" }

    def run(self):
        print ("%s－－－＞启动"%self.threadName)
        while not PAGE_EXIT:
            try:
                # 取出一个数字，先进先出
                # 可选参数block，默认值为True
                # 1. 如果对列为空，block为True的话，不会结束，会进入阻塞状态，直到队列有新的数据
                # 2. 如果队列为空，block为False的话，就弹出一个Queue.empty()异常，
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                html = requests.get(url,headers = self.headers).text
                self.dataQueue.put(html)
                time.sleep(1)

            except Exception,e:
                pass
        print ("%s－－－＞结束" % self.threadName)
        

# 读取存储线程
class parseThread(threading.Thread):
    def __init__(self,threadName,lock,dataQueue,fileName):
        super(parseThread,self).__init__()
        self.threadName = threadName
        self.lock = lock
        self.dataQueue = dataQueue
        self.fileName = fileName

    def run(self):
        print ("%s－－－＞启动" % self.threadName)

        while  not PARSE_EXIT :
            try:
                # 取出一个html源码解析
                qiubaiHtml = self.dataQueue.get(False)
                self.parse(qiubaiHtml)

            except Exception,e:
                pass
        print ("%s－－－＞结束" % self.threadName)

    # 解析html，存入json文件
    def parse(self,qiubaiHtml):
        soup = BeautifulSoup(qiubaiHtml, "lxml")
        # 模糊匹配
        duanzi_list = soup.find_all(id=re.compile(r"qiushi_tag_.*?"))
        for soup_note in duanzi_list:
            #soup_note = BeautifulSoup(note,"lxml")
            # 用户名
            username = soup_note.select('div[class="author clearfix"] h2' )[0].get_text()
            # print username
            # 图片链接
            img_url = []
            imgUrl_list = soup_note.select('a img')
            if(len(imgUrl_list)> 0):
                img = soup_note.select('a img')[0].get("src")
                img_url.append("http"+img[:img.rfind("?")] )

            # 段子
            duanzi = soup_note.select('a div span')[0].get_text()
            # 点赞数
            zan = soup_note.select('div[class="stats"] span i')[0].get_text()
            # 评论数
            pinglun = soup_note.select('div[class="stats"] span i')[1].get_text()

            items = {
                "username":username,
                "img_url":img_url,
                "duanzi":duanzi,
                "zan":zan,
                "pinglun":pinglun
            }
            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁

            with self.lock:
                self.fileName.write(json.dumps(items,ensure_ascii=False).encode("utf-8")+"\n")




# 调控室
def main():

    # 创建锁
    lock = threading.Lock()
    fileText = "0300_多线程爬取糗百.json"
    # if (os.path.exists(fileText)):
    #     print ("删除原文件并将从新创建")
    #     os.remove(fileText)
    fileName = open(fileText.decode("utf-8"),"a")


    pageQueue = Queue(11)
    for i in range(10,18):
        pageQueue.put(i)

    # 采集结果(每页的HTML源码)的数据队列，参数为空表示不限制
    dataQueue = Queue()

    # 采集线程创建与启动
    spiderList = ["采集线程1号","采集线程2号","采集线程3号"]
    threadList = []
    for spiderName in  spiderList:
        thread = spiderThread(spiderName,pageQueue,dataQueue)
        thread.start()
        threadList.append(thread)



    # 解析线程创建与启动
    parseThreadList = ["解析线程1号", "解析线程2号", "解析线程3号"]
    parseList = []
    for threadName in parseThreadList:
        thread = parseThread(threadName,lock,dataQueue,fileName)
        thread.start()
        parseList.append(thread)


    # 等待爬取队列全部被拿完
    while not pageQueue.empty():
        pass
    print ("pageQueue已经被拿空")
    global PAGE_EXIT
    PAGE_EXIT = True

    for thread in threadList:
        thread.join()
        print (str(thread)+"-->join")

    # 等待解析队列全部被拿完
    while not dataQueue.empty():
        pass
    print ("dataQueue已经被拿空")
    global PARSE_EXIT
    PARSE_EXIT = True
    for thread in parseList:
        thread.join()
        print (str(thread.name)+"-->join")

    time.sleep(1)

    with lock:
        # 最后关闭文件流
        fileName.close()

    print "爬取结束，谢谢使用！"



if __name__ == '__main__':
    main()

