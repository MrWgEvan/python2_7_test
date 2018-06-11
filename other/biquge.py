# coding:utf-8

import requests,random
from lxml import etree
import pymongo,codecs,time


class biquge():

    def __init__(self):
        self.headers = {
            "Accept-Language" : "zh - CN, zh;q = 0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
        }
        self.proxies = ["183.159.80.44:18118","60.182.190.120:40723","115.46.77.127:8123",
                        "113.120.61.33:40870","183.159.95.96:18118"]
        self.proxy = {"http": "http://{}".format(random.choice(self.proxies))}

    def get_url(self,url):
        response = requests.get(url=url,proxies = self.proxy,headers=self.headers)
        html = etree.HTML(response.text)
        title_url = html.xpath('//div[@id="list"]/dl/dd[position()>9]/a/@href')
        # print title_url
        # print  response.text
        return title_url

    def get_content(self,url):
        response = requests.get(url=url, proxies=self.proxy, headers=self.headers)
        html = etree.HTML(response.text)
        title= html.xpath('//div[@class="bookname"]/h1/text()')[0]
        print (title + "       ok-----------")
        content_list= html.xpath('//div[@id="content"]/text()')
        content = "".join(content_list)
        item = {
            "title":title,
            "content":content
        }
        return item

    def insert_mongo(self,item,host,port,dbName, collectionName):
        host = host
        port = port
        dbName = dbName
        collectionName = collectionName
        c2 = pymongo.MongoClient(host=host,port=port)
        db = c2[dbName]
        shengxu = db[collectionName]
        data = dict(item)
        shengxu.insert(data)


    def start_spider(self):
        host = "127.0.0.1"
        port = 27017
        dbName = "biquge"
        collectionName = "shengxu"
        title_url = self.get_url("https://www.biquge5200.com/52_52542/")
        for url in title_url:
            item = self.get_content(url=url)
            self.insert_mongo(item,host,port,dbName,collectionName)
            time.sleep(1)


if __name__ == '__main__':
    bqg = biquge()
    bqg.start_spider()



