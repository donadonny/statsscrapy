# -*- coding: utf-8 -*-
"""爬取国家统计局数据中国的年度、季度、月度指标树"""
import scrapy
import json

from statscrapy.items import ZbTtem

class GjstatsSpider(scrapy.Spider):
    name = "gjstats"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        'http://data.stats.gov.cn/easyquery.htm?id=&dbcode=hgjd&wdcode=zb&m=getTree',
    )

    def parse(self, response):
        zb = ZbTtem()
        zbfls = json.loads(response.body_as_unicode())
        for i in range(len(zbfls)):
            zbfl = zbfls[i]
            zb["dbcode"] = zbfl['dbcode']
            zb['id'] = zbfl['id']
            zb['isParent'] = zbfl['isParent']
            zb['name'] = zbfl['name']
            zb['pid'] = zbfl['pid']
            zb['wdcode'] = zbfl['wdcode']
            yield zb