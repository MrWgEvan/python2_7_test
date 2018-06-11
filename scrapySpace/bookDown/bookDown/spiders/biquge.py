# -*- coding: utf-8 -*-


import scrapy
from scrapy.selector import Selector
from bookDown.items import BookdownItem

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.biquge5200.com']
    start_urls = ['https://www.biquge5200.com/']

    def parse(self, response):

        book_list = Selector(response).xpath(r'//div[@id="main"]/div[2]//a')

        for book in book_list:
            book_href = book.xpath(r'./@href')[0].extract()
            book_name = book.xpath(r'./text()')[0].extract()

            yield scrapy.Request(url=book_href,callback=self.get_url,meta={"book_name":book_name})

    def get_url(self,response):

        title_url = Selector(response).xpath(r'//div[@id="list"]/dl/dd[position() > 9]/a/@href').extract()
        for title in title_url:
            yield scrapy.Request(url=title,callback=self.get_content,meta={"book_name":response.meta['book_name']})

    def get_content(self,response):
        item = BookdownItem()

        title = Selector(response).xpath(r'//div[@class="bookname"]/h1/text()')[0].extract()
        print (title + "       ok-----------")
        content_list = Selector(response).xpath(r'//div[@id="content"]/text()').extract()
        content = "".join(content_list)

        item["title"] = title
        item["content"] = content
        item["url"] = response.url
        item["bookName"] = response.meta["book_name"]

        yield item
