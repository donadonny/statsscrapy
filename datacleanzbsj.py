"""本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标数据"""
import sqlite3
import pymongo
import json
conn = sqlite3.connect('test.db')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.items
zbfl = db.zbfl
sjyss = zbfl.find({"data":{"$exists":"true"}})
for sjys in sjyss:
    for sj in sjys['data']['datanodes']:
        data = sj['data']['data']
        doccount = sj['data']['dotcount']
        strdata = sj['data']['strdata']
        hasdata = sj['data']['hasdata']
        zbcode = sj['wds'][0]['valuecode']
        sj = sj['wds'][1]['valuecode']
        dq = "全国"
        if hasdata:
            conn.execute("INSERT INTO zbsj(zbcode, sj, data, doccount, strdata, dq) VALUES (?,?,?,?,?,?)",(zbcode, sj, data, doccount, strdata, dq))
            conn.commit()
        else:
            pass
conn.close()
