# -*- coding: utf-8 -*-
"""爬取国家统计局数据中国的年度、季度、月度指标树"""
import scrapy
import json
from scrapy.loader import ItemLoader
from scrapy.http import Request

from statscrapy.items import ZbTtem

class GjstatsSpider(scrapy.Spider):
    name = "gjstats"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        #'http://data.stats.gov.cn/easyquery.htm?id=&dbcode=hgjd&wdcode=zb&m=getTree',
        #'http://data.stats.gov.cn/easyquery.htm?id=&dbcode=hgnd&wdcode=zb&m=getTree',
        'http://data.stats.gov.cn/easyquery.htm?id=&dbcode=hgyd&wdcode=zb&m=getTree',
    )

    def parse(self, response):
        zb = ZbTtem()
        #zb = ItemLoader(item=ZbTtem(),response=response)
        zbfls = json.loads(response.body_as_unicode())
        for i in range(len(zbfls)):
            zbfl = zbfls[i]
            zb["dbcode"] = zbfl['dbcode']
            zb['id'] = zbfl['id']
            zb['isParent'] = zbfl['isParent']
            zb['name'] = zbfl['name']
            zb['pid'] = zbfl['pid']
            zb['wdcode'] = zbfl['wdcode']

            if zb['isParent']:
                zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?id=' +zb['id']+ '&dbcode='+ zb['dbcode'] +'&wdcode=zb&m=getTree'
                yield Request(zb['urlnext'],callback=self.parse_item)

            else:
                zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode='+ zb['dbcode'] +'&rowcode='+ zb['wdcode']+'&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"'+zb['id']+'"},{"wdcode":"sj","valuecode":"LAST2000"}]&k1=1474175295353'
                yield Request(zb['urlnext'], callback=self.parse_table)
            yield zb

    def parse_item(self, response):
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

            if zb['isParent']:
                zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?id=' + zb['id'] + '&dbcode='+ zb['dbcode'] +'&wdcode=zb&m=getTree'
                yield Request(zb['urlnext'], callback=self.parse_item)
            else:
                zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode='+ zb['dbcode'] +'&rowcode='+ zb['wdcode']+'&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"'+zb['id']+'"},{"wdcode":"sj","valuecode":"LAST2000"}]&k1=1474175295353'
                yield Request(zb['urlnext'], callback=self.parse_table)
            yield zb

    def parse_table(self,response):
        zb = ZbTtem()
        data = json.loads(response.body_as_unicode())
        zb['data'] = data['returndata']
        yield zb



