# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import Request

from statscrapy.items import ZbTtem,DqItem


class FsydSpider(scrapy.Spider):
    name = "fsyd"
    allowed_domains = ["data.stats.gov.cn"]
    start_urls = (
        'http://data.stats.gov.cn/easyquery.htm?dbcode=fsyd&id=zb&m=getTree&wdcode=zb',
    )
    # def parse_item(self, response):
    #     zb = ZbTtem()
    #     zbfls = json.loads(response.body_as_unicode())
    #     yield Request('http://data.stats.gov.cn/easyquery.htm?m=getOtherWds&dbcode=fsjd&rowcode=zb&colcode=sj&wds=[]&k1=1474864542914',callback=self.parse_table)
    #     for i in range(len(zbfls)):
    #         zbfl = zbfls[i]
    #         zb["dbcode"] = zbfl['dbcode']
    #         zb['id'] = zbfl['id']
    #         zb['isParent'] = zbfl['isParent']
    #         zb['name'] = zbfl['name']
    #         zb['pid'] = zbfl['pid']
    #         zb['wdcode'] = zbfl['wdcode']
    #
    #         if zb['isParent']:
    #             zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?id=' + zb['id'] + '&dbcode=' + zb[
    #                 'dbcode'] + '&wdcode=zb&m=getTree'
    #             yield Request(zb['urlnext'], callback=self.parse_item)
    #         else:
    #             zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=' + zb['dbcode'] + '&rowcode=' + \
    #                             zb['wdcode'] + '&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"' + zb[
    #                                 'id'] + '"},{"wdcode":"sj","valuecode":"LAST2000"}]&k1=1474175295353'
    #             yield Request(zb['urlnext'], callback=self.parse_table)
    #         yield zb
    #
    def parse_dq(self, response):
        dq = DqItem()
        data = json.loads(response.body_as_unicode())
        for  i in range(len(data['returndata'][0]['nodes'])):
            dq['dqdm'] = data['returndata'][0]['nodes'][i]['code']
            dq['dqmc'] = data['returndata'][0]['nodes'][i]['name']
            yield dq
            # print(dq)
        'data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&wds=[{"wdcode":"reg","valuecode":"110000"}]&dfwds=[]&k1=1474864543454'

    # def parse_table(self, response):
    #     zb = ZbTtem()
    #     data = json.loads(response.body_as_unicode())
    #     zb['data'] = data['returndata']
    #     yield zb


    def parse(self, response):
        zb = ZbTtem()
        dq = DqItem()
        # zb = ItemLoader(item=ZbTtem(),response=response)
        zbfls = json.loads(response.body_as_unicode())
        yield Request('http://data.stats.gov.cn/easyquery.htm?m=getOtherWds&dbcode=fsjd&rowcode=zb&colcode=sj&wds=[]&k1=1474864542914',callback=self.parse_dq)
        print(dq)
        # for i in range(len(zbfls)):
        #     zbfl = zbfls[i]
        #     zb["dbcode"] = zbfl['dbcode']
        #     zb['id'] = zbfl['id']
        #     zb['isParent'] = zbfl['isParent']
        #     zb['name'] = zbfl['name']
        #     zb['pid'] = zbfl['pid']
        #     zb['wdcode'] = zbfl['wdcode']
        #
        #     if zb['isParent']:
        #         zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?id=' + zb['id'] + '&dbcode=' + zb[
        #             'dbcode'] + '&wdcode=zb&m=getTree'
        #         yield Request(zb['urlnext'], callback=self.parse_item)
        #
        #     else:
        #         zb['urlnext'] = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=' + zb['dbcode'] + '&rowcode=' + \
        #                         zb['wdcode'] + '&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"' + zb[
        #                             'id'] + '"},{"wdcode":"sj","valuecode":"LAST2000"}]&k1=1474175295353'
        #         yield Request(zb['urlnext'], callback=self.parse_table)
        #     yield zb

        #'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsyd&rowcode=zb&colcode=sj&dfwds=[{"wdcode":"zb","valuecode":"A1401"}]&k1=1474867237651&wds=[{"wdcode":"reg","valuecode":"110000"}]'

        '''先按照原有逻辑组装url，然后在最后拼接地区选项，完成最后的组装后执行数据的爬取'''