# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sun0769.items import Sun0769Item
from scrapy.selector import Selector


class DongSpider(CrawlSpider):
    name = 'dong'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    page_list = LinkExtractor(allow=r'type=4&page')
    question_list = LinkExtractor(allow=r'question/\d+/\d+.shtml')

    '''用rules中的规则从html（或xml）文本中提取匹配的链接，通过这个链接再次生成Request，
    如此不断循环，直到返回的文本中再也没有匹配的链接，或调度器中的Request对象用尽，程序才停止。
    callback： 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，
    该回调函数接受一个response作为其第一个参数。'''
    rules = (
        #Rule(pagelink, process_links = "deal_links", follow = True),
        Rule(page_list,callback='page_parse', follow=True),
        Rule(question_list, callback='parse_item', follow=False)
    )

    def page_parse(self,response):
        print response.url

    # # 需要重新处理每个页面里的链接，将链接里的‘Type&type=4?page=xxx’替换为‘Type?type=4&page=xxx’（或者是Type&page=xxx?type=4’替换为‘Type?page=xxx&type=4’），否则无法发送这个链接
    # def deal_links(self, links):
    #     for link in links:
    #         link.url = link.url.replace("?", "&").replace("Type&", "Type?")
    #         print link.url
    #     return links

    def parse_item(self, response):

        item = Sun0769Item()

        question = Selector(response).xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        title = question.strip().split(u'编号:')[0]
        #.strip().split(' ')[0]
        #.split(r'：')[-1]
        number = question.strip().split(' ')[-1].split(':')[-1]

        content = Selector(response).xpath("//div[@class='pagecenter p3']//div[@class='contentext']/text()").extract()
        # 有图片时
        if len(content) == 0:
            content = Selector(response).xpath(
                " //div[@class='pagecenter p3']//div[@class='c1 text14_2']/text()").extract()
            item["content"] = "".join(content).strip()
        else:
            img = Selector(response).xpath("//div[@class='pagecenter p3']//img/@src").extract()
            item["img"] = img
            item["content"] = "".join(content).strip()

        item["title"] = title
        item["number"] = number
        item["url"] = response.url

        yield item


