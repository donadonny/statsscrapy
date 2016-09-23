"""本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标分类，后修改为将数据清洗后返回存储到mongodb中"""
import pymongo
import json
from pymongo import MongoClient



client = MongoClient('localhost', 27017)
db = client.items
zbfl = db.zbfl


#第一版本，插入数据到sqlit的语句
#     uid = str(fl['_id'])
#     url = fl['urlnext']
#     name = fl['name']
#     pid = fl['pid']
#     dbcode = fl['dbcode']
#     wdcode = fl['wdcode']
#     id = fl['id']
#     isParent = fl['isParent']
#     #插入数据到sqlite
#     conn.execute("INSERT INTO zbfl(id,name,url,pid,dbcode,wdcode,uid,isParent) VALUES (?,?,?,?,?,?,?,?)",(id,name,url,pid,dbcode,wdcode,uid,isParent))
#     conn.commit()
# conn.close()
#
# """本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标信息"""
# '''清晰指标元数据'''
def zbclean():
    try:
        indi = stats.indi
    except:
        indi = pymongo.create_collection('indi')
    for zb in zbfl.find({"data":{"$exists":"true"}}):
        post = zb['data']['wdnodes'][0]['nodes']
        stats.indi.insert_many(post)
#     uid = str(zb['_id'])
#     code = zb['data']['wdnodes'][0]['nodes'][0]['code']
#     name = zb['data']['wdnodes'][0]['nodes'][0]['name']
#     cname = zb['data']['wdnodes'][0]['nodes'][0]['cname']
#     exp = zb['data']['wdnodes'][0]['nodes'][0]['exp']
#     unit = zb['data']['wdnodes'][0]['nodes'][0]['unit']
#     #插入数据到sqlite
#     conn.execute("INSERT INTO zb(uid,code,name,cname,exp,unit) VALUES (?,?,?,?,?,?)",(uid,code,name,cname,exp,unit))
#     conn.commit()
# conn.close()

# """本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标数据"""
# #在find函数中设置不会超时
# #sjyss = zbfl.find({"data":{"$exists":"true"}})
# #一定要在使用完之后释放连接，不然会一直占用系统资源
# '''清洗指标数据'''
def zbdataclean():
    try:
        indi_data = stats.indi
    except:
        indi_data = pymongo.create_collection('indi_data')


    for sjys in zbfl.find({"data":{"$exists":"true"}}).batch_size(10).max_time_ms(20000):
        for sj in sjys['data']['datanodes']:
            post = {}
            post['data'] = sj['data']['data']
            post['doccount'] = sj['data']['dotcount']
            post['strdata'] = sj['data']['strdata']
            post['hasdata'] = sj['data']['hasdata']
            post['zbcode'] = sj['wds'][0]['valuecode']
            post['sj'] = sj['wds'][1]['valuecode']
            post['dq'] = "全国"
            if post['hasdata']:
                stats.indi_data.insert_one(post)
                    #插入数据到sqlite
                    # conn.execute("INSERT INTO zbsj(zbcode, sj, data, doccount, strdata, dq,uid) VALUES (?,?,?,?,?,?,?)",(zbcode, sj, data, doccount, strdata, dq,uid))
                    # conn.commit()
                    # client.close()
            # else:
            #      continue
    #             client.close()
    # conn.close()

'''清洗指标分类数据'''
#def zbflclean(): 找不到如何让scrapy调用方法前，暂时无法将这个做成方法。
try:
    stats = client.stats
except:
    stats = db.create_database('stats')
try:
    indi_fl = stats.indi_fl
except:
    indi_fl = pymongo.create_collection('indi_fl')
for fl in zbfl.find({"wdcode":"zb"}):
    stats.indi_fl.insert_one(fl)
zbclean()
zbdataclean()