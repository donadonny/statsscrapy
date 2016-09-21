"""本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标数据"""
import sqlite3
import pymongo
import json
conn = sqlite3.connect('test.db')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.items
zbfl = db.zbfl
#在find函数中设置不会超时
#sjyss = zbfl.find({"data":{"$exists":"true"}})
#一定要在使用完之后释放连接，不然会一直占用系统资源

for sjys in zbfl.find({"data":{"$exists":"true"}}).batch_size(10).max_time_ms(200):
    uid = str(sjys['_id'])
    for sj in sjys['data']['datanodes']:
        data = sj['data']['data']
        doccount = sj['data']['dotcount']
        strdata = sj['data']['strdata']
        hasdata = sj['data']['hasdata']
        zbcode = sj['wds'][0]['valuecode']
        sj = sj['wds'][1]['valuecode']
        dq = "全国"
        if hasdata:
            try:
                conn.execute("INSERT INTO zbsj(zbcode, sj, data, doccount, strdata, dq,uid) VALUES (?,?,?,?,?,?,?)",(zbcode, sj, data, doccount, strdata, dq,uid))
                conn.commit()
                client.close()
            except:
                continue

        else:
            client.close()
conn.close()
