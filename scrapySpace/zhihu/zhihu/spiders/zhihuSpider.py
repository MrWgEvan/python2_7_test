# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule,Spider
from scrapy.selector import Selector
from scrapy import Request,FormRequest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from zhihu.items import ZhihuItem
import time,re,json





class ZhihuspiderSpider(CrawlSpider):
    name = 'zhihuSpider'
    allowed_domains = ['www.zhihu.com']
    start_urls = [ 'https://www.zhihu.com/topic']


    list = LinkExtractor(allow = (r'/question/\d+', ))
    rules = (
        Rule(list, callback="parse_item",follow=True),
     )


    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        url = "https://www.zhihu.com/signup"
        chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        chrome_option.add_argument('window-size=1360x768')  # 指定浏览器分辨率
        driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_option)
        driver.get(url)
        login = driver.find_element_by_xpath(r"//span[@data-reactid='93']")
        ActionChains(driver).move_to_element(login).click(login).perform()

        driver.find_element_by_xpath(r'//input[@name="username"]').send_keys("18665924017")
        driver.find_element_by_xpath(r'//input[@name="password"]').send_keys("2ghlmcL")
        btn_login = driver.find_element_by_xpath(r'//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]')
        ActionChains(driver).move_to_element(btn_login).click(btn_login).perform()
        #return self.parse_login(url)
        time.sleep(3)
        driver.save_screenshot("zhihu.png")
        # cookies = driver.get_cookies()[-1]
        # print cookies
        cookies = {}
        for cookie in driver.get_cookies():
            cookies[cookie["name"]] = cookie["value"]

        driver.quit()

        response = FormRequest(url="https://www.zhihu.com/",cookies=cookies,callback=self.after_login,meta={'cookiejar':1})
        return [response]

    def after_login(self,response):
        # urlList = Selector(response).xpath(r'//a[contains(@href,"/question/")]/@href').extract()
        # urlList2 = []
        # for i in urlList:
        #     if (re.search(r'.*?/answer/\d+', i)):
        #         urlList2.append(i)
        # urlL = list(set(urlList) - set(urlList2))
        # for url in urlL:
        #     yield self.make_requests_from_url("https://www.zhihu.com"+url,response)
        return self.make_requests_from_url(self.start_urls[0],response)

    def make_requests_from_url(self, url,response):
        """ This method is deprecated. """

        return Request(url, dont_filter=False,meta={"cookiejar":response.meta["cookiejar"]},callback=self.parse_item)

    def parse_item(self, response):
        #print response.meta["cookies"]

        for each in Selector(response).xpath(r'//div[@class="Card AnswerCard"] | //div[@class="Card MoreAnswers"]'):
            item = ZhihuItem()
            item["authorName"] =  Selector(each).xpath(r'.//span[@class="UserLink AuthorInfo-name"]//a/text()').extract()[0]

            item["authorUrl"] = Selector(each).xpath(r'.//div[@class="ContentItem-meta"]//meta[@itemprop="url"]/@content').extract()[0]
            item["url"] = response.url

            yield item
            print '11111'





