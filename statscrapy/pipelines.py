# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class StatscrapyPipeline(object):
    collection_name = 'zbfl'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]



    def process_item(self, item, spider):
        if spider.name == 'csnd':
            self.collection_name='csnd'
        elif spider.name =='csyd':
            self.collection_name ='csyd'
        elif spider.name == 'fsjd':
            self.collection_name = 'fsjd'
        elif spider.name == 'fsnd':
            self.collection_name = 'fsnd'
        elif spider.name == 'fsyd':
            self.collection_name = 'fsyd'
        elif spider.name == 'gjstats':
            self.collection_name = 'zbfl'
        self.db[self.collection_name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()