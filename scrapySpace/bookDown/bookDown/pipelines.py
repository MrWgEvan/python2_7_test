# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo


class BookdownPipeline(object):

    def __init__(self):
        self.host = settings['MONGO_HOST']
        self.port = settings['MONGO_PORT']
        self.client = pymongo.MongoClient(host=self.host,port=self.port)
        self.dbName = self.client[ settings['MONGO_DB']]

    def process_item(self, item, spider):

        collectionName = item['bookName']
        collection_name = self.dbName[collectionName]
        data = dict(item)
        collection_name.insert(data)

        return item
