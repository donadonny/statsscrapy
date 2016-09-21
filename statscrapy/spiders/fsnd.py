# -*- coding: utf-8 -*-
import scrapy


class FsndSpider(scrapy.Spider):
    name = "fsnd"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        'http://data.stats.gov.cn/easyquery.htm?dbcode=fsnd&id=zb&m=getTree&wdcode=zb',
    )

    def parse(self, response):
        pass
