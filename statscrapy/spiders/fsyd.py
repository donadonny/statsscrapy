# -*- coding: utf-8 -*-
import scrapy


class FsydSpider(scrapy.Spider):
    name = "fsyd"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        'http://data.stats.gov.cn/easyquery.htm?dbcode=fsyd&id=zb&m=getTree&wdcode=zb',
    )

    def parse(self, response):
        pass
