# -*- coding: utf-8 -*-


import scrapy
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aLinux']


    def parse(self, response):
        #with open("itcast.html","w") as f:
        #    f.write(response.body)

        items = []

        # class 以tea_txt开头的div  //div[starts-with(@class,"tea_txt")]

        # for each in response.xpath('//div[@class="li_txt"]'):
        #     # 实例化
        #     item = MyspiderItem()
        #
        #     # extract()返回unicode字符串
        #     namelist = each.xpath('h3/text()').extract()
        #     discriptionlist = each.xpath('p/text()').extract()
        #     #imglist = response.xpath('//div[@class="tea_txt"]//img/@data-original').extract()
        #
        #     item['name'] = namelist[0].encode("gbk").strip()
        #     #item['img'] = imglist[i].encode("gbk")
        #     item['discription'] = discriptionlist[0].encode("gbk").strip()
        #     items.append(item)

        for each in response.xpath('//div[@class="tea_con"]/div//li'):
            #print each
            # 实例化
            item = MyspiderItem()

            # extract()返回unicode字符串
            namelist = each.xpath('.//h3/text()').extract()
            #print namelist[0]
            discriptionlist = each.xpath('.//p/text()').extract()
            imglist = each.xpath('./img/@data-original').extract()

            item['name'] = namelist[0].encode("gbk").strip()
            item['img'] = imglist[0].encode("gbk")
            item['discription'] = discriptionlist[0].encode("gbk").strip()
            items.append(item)

        return items
