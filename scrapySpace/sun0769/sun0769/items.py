# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Sun0769Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    # 标题
    title= scrapy.Field()
    # 编号
    number= scrapy.Field()
    # 内容
    content=scrapy.Field()
    # url
    url = scrapy.Field()
    img = scrapy.Field()


