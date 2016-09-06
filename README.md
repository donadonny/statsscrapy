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
