#-*- coding: UTF-8 -*-
import re
import urllib

def htmlpy(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def imgUrl(html):
    reg =  r'src="(.*?\.jpg)" pic_ext'
    imgurl = re.compile(reg)
    urlList = imgurl.findall(html)
    #urlList = re.findall(imgurl,html)
    x = 0
    for img in urlList:
        urllib.urlretrieve(img,'fj%s.jpg' %x )
        x+=1
    print "搞定收工，真帅！"

if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/2369102942"
    html = htmlpy(url)
    imgUrl(html)





