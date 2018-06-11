# -*-coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import json
import os

class Spider():
    def __init__(self):
        self.page = raw_input("请输入要爬取第几页：")
        self.url = "http://www.qiushibaike.com/8hr/page/"+self.page+"/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36" }

    def bs4glist(self,html):
        soup = BeautifulSoup(html,"lxml")
        # 模糊匹配
        duanzi_list = soup.find_all(id = re.compile(r"qiushi_tag_.*?"))
        return duanzi_list

    def getHtml(self):
        html = requests.get(self.url,headers = self.headers).text
        return html

    def get_duanzi(self):
        html = self.getHtml()
        duanzi_list = self.bs4glist(html)
        print len(duanzi_list)
        if(os.path.exists("qiubai.json")):
            os.remove("qiubai.json")
        for soup_note in duanzi_list:
            #soup_note = BeautifulSoup(note,"lxml")
            # 用户名
            username = soup_note.select('div[class="author clearfix"] h2' )[0].get_text().strip()
            print username
            # 图片链接
            img_url = []
            imgUrl_list = soup_note.select('a img')
            if(len(imgUrl_list)> 0):
                img = soup_note.select('a img')[0].get("src").strip()
                img_url.append("http"+img[:img.rfind("?")] )

            # 段子
            duanzi = soup_note.select('a div span')[0].get_text().strip()
            # 点赞数
            zan = soup_note.select('div[class="stats"] span i')[0].get_text().strip()
            # 评论数
            pinglun = soup_note.select('div[class="stats"] span i')[1].get_text().strip()

            # .findAll("span", {"class":{"green", "red"}})


            items = {
                "username":username,
                "img_url":img_url,
                u"段子":duanzi,
                # "duanzi":duanzi,
                "zan":zan,
                "pinglun":pinglun
            }
            with open("qiubai.json","a") as f:
                f.write(json.dumps(items,ensure_ascii=False).encode("utf-8")+"\n")
        print "搞定"

        # print (duanzi_list)



if __name__ == '__main__':
    spider = Spider()
    spider.get_duanzi()


