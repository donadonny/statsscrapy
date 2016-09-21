# -*- coding: utf-8 -*-
import scrapy


class CsydSpider(scrapy.Spider):
    name = "csyd"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        'http://data.stats.gov.cn/easyquery.htm?dbcode=csyd&id=zb&m=getTree&wdcode=zb',
    )

    def parse(self, response):
        pass
