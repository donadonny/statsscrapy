# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StatscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dataNum = scrapy.Field(serializer=str)
    #地区来源
    areaSource = scrapy.Field()
    #数据来源
    dataSource = scrapy.Field()
    #时间
    dataTime = scrapy.Field()
    #表名
    reportName = scrapy.Field()
    #数据内容
    dataContent = scrapy.Field()
    #计量单位
    dataUnit = scrapy.Field()
