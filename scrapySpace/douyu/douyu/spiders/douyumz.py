# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json,time


class DouyumzSpider(scrapy.Spider):
    name = 'douyumz'
    allowed_domains = ['apiv2.douyucdn.cn']
    offect = 0
    # left_url = 'https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/1_8/'
    # right_url = '/20/android?client_sys=android'
    # start_urls = [left_url+str(offect)+right_url]
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url+str(offect)]

    # 禁止网页重定向
    meta = {
        "dont_redirect":True
    }

    def parse(self, response):
        #data = json.loads(response.body)['data']['list']
        data = json.loads(response.body)['data']
        #if data :

        for each in data:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['smallImage'] = each['room_src']

            yield item

        #if(self.offect < 100):
        self.offect += 20

        # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
        request = scrapy.Request(self.url + str(self.offect), callback=self.parse,dont_filter=True,meta=self.meta)
        time.sleep(1)
        yield request