# statsscrapy
目的：用scrapy爬取统计局发布的数据，提取为结构化数据。
项目总体步骤：
  1、选取年鉴数据作为爬取对象。
  2、以其中某一个表的数据为起始点，将数据爬取到。
  3、提取地区来源、数据来源、时间、表名、以及数据内容。
  4、将数据内容提取：时间、地区、指标、计量单位。
  5、将指标映射出分组和指标。
选择浙江省统计年鉴为起始，因为该统计年鉴为网页格式，而不是图片。
浙江省2015年统计年鉴地址：http://www.zj.stats.gov.cn/tjsj/tjnj/DesktopModules/Reports/12.%E6%B5%99%E6%B1%9F%E7%BB%9F%E8%AE%A1%E5%B9%B4%E9%89%B42015/indexch.htm
选择工业和能源的7-1表作为起始，地址为：
http://www.zj.stats.gov.cn/tjsj/tjnj/DesktopModules/Reports/12.%E6%B5%99%E6%B1%9F%E7%BB%9F%E8%AE%A1%E5%B9%B4%E9%89%B42015/indexch.htm
另外，各省统计年鉴多提供excel文件形式，下一步用scrapy获取年鉴信息后，整理excel的下载链接，并下载文件。



查找国家统计局数据规律
http://data.stats.gov.cn/easyquery.htm?id=A03&dbcode=hgjd&wdcode=zb&m=getTree
上面的网址可以获取指标树，但只有一层，另外子层规律尚未得知，其中id为对应的指标ID，dbcode为类型，目前有hgnd年度，hgjd季度，hgyd月度，wdcode为zd为指标。将获取的第一层ID传递过去，则可以得到下层的ID。检查是否父亲属性为true的即可下钻。

http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"A030701"},{"wdcode":"sj","valuecode":"LAST20"}]&k1=1474175295353
以上网址为查询对应的数据结果，其中wdcode的zd为指标，valuecode的A030701为左侧的分类代码，从上一步骤的网址中获取，wdcode的sj推测为时间的意思，valuecode的LAST20，为近20个期别，最后的k1以及一串数字，不知到什么意思。

具体的时间参数为

{"returncode":200,"returndata":[
  {"issj":true,"nodes":[
      {"code":"LAST5","name":"最近5年","sort":"4"},
      {"code":"LAST10","name":"最近10年","sort":"4"},
      {"code":"LAST20","name":"最近20年","sort":"4"}
      ],
      "selcode":"last10","wdcode":"sj","wdname":"时间"}
    ]
}

说明：
    当前程序还仅仅能爬取数据，然后清洗为可用格式（类似结构化存储的样式）。尚需要进一步完善的内容：
    1、爬取部门和国际数据，因为是同形式。
    2、爬取链接，下载Excel文件，并解析。
    3、处理增量爬取过程。
    4、处理不同爬虫存储不同集合问题。
    5、处理爬取完成后自动清洗功能。
    6、处理增量清洗功能。
    7、爬取其他网页中的数据。