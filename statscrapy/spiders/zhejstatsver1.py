#时间：2016-9-06
#作者：Simon
#用途：创建第一个样例爬虫，爬取一个固定页面的表格数据。
import scrapy
from statscrapy.items import StatscrapyItem

class zhejver1(scrapy.Spider):
    name = 'zhejver1'

    allowed_domains = ['http://www.zj.stats.gov.cn']

   # start_urls = ['http://www.zj.stats.gov.cn/tjsj/tjnj/DesktopModules/Reports/12.浙江统计年鉴2015/indexch.htm']   页面中间包含着页面，暂时不会处理，放弃。
    start_urls = ['http://www.gdstats.gov.cn/tjsj/gy/gyzjz/201604/t20160405_326133.html']

    def parse(self,response):
        item = StatscrapyItem()
        item['areaSource'] = "浙江省"
        item['dataSource'] = "工业进度数据"
        item['dataTime'] = "2016年2月"
        item['reportName'] = response.xpath('//div[@id="xlcontent"]/div[2]/div[1]/h4/text()').extract()
        item['dataUnit'] =  response.xpath('//div[@id="xlcontent"]/div[2]/div[1]/h4/text()').extract()
        item['dataContent'] =  response.xpath('//table[@class="MsoNormalTable"]')
        print(item)
        return item