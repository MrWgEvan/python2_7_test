# coding:utf-8
import urllib
import urllib2
import  re

class ImgDow:

    def __init__(self):
        self.tieba = raw_input("请输入要爬的贴吧：")
        self.start_page = raw_input("请输入爬取开始的页面：")
        self.end_page = raw_input("请输入爬取截止的页面：")
        self.url = "http://tieba.baidu.com"
        self.header = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36" }

    def page_down(self,url):
        request = urllib2.Request(url, headers=self.header)
        html = urllib2.urlopen(request).read()
        return html

    def find_tiezi_link(self,html):

        pattern = re.compile(r'<a.*?href="(/p/.*?)"\s*tit',re.S)
        list = pattern.findall(html)

        return list

    def img_down(self,img_list):
        for i in img_list:
            img_name = i[-8:]
            print ("正在处理图片{0}".format(img_name) )
            request = urllib2.Request(url=i,headers=self.header)
            img = urllib2.urlopen(request).read()
            with open("photo/"+str(img_name),"wb") as f:
                f.write(img)
        print ("一共"+str(len(img_list))+"张图片全部下载完毕！！！")

    def img_list(self,url_list):
        img_list = []
        for i in url_list:
            tiezi_url = self.url+i
            request = urllib2.Request(tiezi_url, headers=self.header)
            html = urllib2.urlopen(request).read()
            pattern = re.compile(r'BDE_Image" src="(.*?)" siz', re.S)
            list = pattern.findall(html)
            img_list += list
        self.img_down(img_list)



    def find_link(self):
        tb_name = {"kw":self.tieba}
        tb_name = urllib.urlencode(tb_name)
        url_list = []
        for i in range(int(self.start_page),int(self.end_page)+1):
            url = self.url+"/f?"+tb_name+"&pn="+str((i-1)*50)
            print ("正在处理第%d页....." % i)
            html = self.page_down(url)
            list =self.find_tiezi_link(html)
            url_list += list
        self.img_list(url_list)

if __name__ == '__main__':
    imgDow = ImgDow()
    imgDow.find_link()
