# -*- coding: utf-8 -*-
import scrapy


class FsjdSpider(scrapy.Spider):
    name = "fsjd"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        'http://data.stats.gov.cn/easyquery.htm?dbcode=fsjd&id=zb&m=getTree&wdcode=zb',
    )

    def parse(self, response):
        pass
