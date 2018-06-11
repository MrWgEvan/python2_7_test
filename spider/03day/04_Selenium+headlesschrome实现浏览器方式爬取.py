# -*-coding:utf-8 -*-

import unittest,time,os
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bf
import json



class panda(unittest.TestCase):
    # 初始化方法，必须是setUp()
    def setUp(self):
        """chromedriver not in PATH出现错误时，在路经前面加上r，不许转义
        """
         # chromedriver的路径
        self.chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        self.chrome_option = Options()
         # 设置为无头模式
        self.chrome_option.add_argument("--headless")
         # 指定chrome浏览器的位置
        #self.chrome_option.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        """
        chrome_option.add_argument('window-size=1920x3000') #指定浏览器分辨率
        chrome_option.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
        chrome_option.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
        chrome_option.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
        """
        # 指定的chrome浏览器创建浏览器对象
        self.driver = webdriver.Chrome(executable_path=self.chromedriver, options=self.chrome_option)

        self.filename = "panda.json"

        # self.driver.delete_all_cookies()
        # self.driver.add_cookie()

    def testPanda(self):
        url="https://www.panda.tv/all"
        self.driver.get(url)

        while True:
            # # driver.page_source网页渲染后的源代码
            soup = bf(self.driver.page_source,"lxml")
            time.sleep(2)


            #房间名 ：
            rooms = soup.select('span[class="video-title"]')
            #主播 ：
            users = soup.select('span[class="video-nickname"]')
            #观众 ：
            viewers = soup.select('span[class="video-station-info"] i')
            #类型　：
            sizes = soup.select('a[class="video-label-item label-color-0"]')

            for room,user,viewer,size in zip(rooms,users,viewers,sizes):
                 items = {
                     "room":room.get_text().strip(),
                     "user":user.get_text().strip(),
                     "viewer":viewer.get_text().strip(),
                     "size":size.get_text().strip()

                     # 'ascii' codec can't decode byte 0xe8 错误，
                     # 解决方法：在中文name前加 u
                     # u"房间号":room,
                 }
                #print u"主播" + room.get_text().strip()

                 with open(self.filename,"a") as f:
                     f.write(json.dumps(items,ensure_ascii=False).encode("utf-8")+"\n")


            # 截图
            # self.driver.save_screenshot("baidu.png")

            if self.driver.page_source.find("j-page-next disabled") != -1:
                break

            self.driver.find_element_by_class_name("j-page-next").click()

    # 测试结束执行的方法
    def tearDown(self):
        print ("爬取pandaTV结束")
        self.driver.quit()


if __name__ == '__main__':
    # 启动测试模块
    print "开始爬取"
    unittest.main()




