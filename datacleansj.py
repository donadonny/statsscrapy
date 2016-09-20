"""本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标信息"""
import sqlite3
import pymongo
import json
conn = sqlite3.connect('test.db')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.items
zbfl = db.zbfl
for zb in zbfl.find({"data":{"$exists":"true"}}):
    uid = str(zb['_id'])
    code = zb['data']['wdnodes'][0]['nodes'][0]['code']
    name = zb['data']['wdnodes'][0]['nodes'][0]['name']
    cname = zb['data']['wdnodes'][0]['nodes'][0]['cname']
    exp = zb['data']['wdnodes'][0]['nodes'][0]['exp']
    unit = zb['data']['wdnodes'][0]['nodes'][0]['unit']
    conn.execute("INSERT INTO zb(uid,code,name,cname,exp,unit) VALUES (?,?,?,?,?,?)",(uid,code,name,cname,exp,unit))
    conn.commit()
conn.close()










#fl = zbfl.find_one({"data":{"$exists":"true"}})
# data= fl['data']
# print(data['wdnodes'][0]['nodes'])


# for wdnode in data['wdnodes']:
#     print(wdnode)
#     # print(wdnode['wdcode'])
#     # print(wdnode['wdname'])
#     # for node in wdnode['nodes']:
#     #     print(node['exp'])
#     #     print(node['nodesort'])
#     #     print(node['tag'])
#     #     print(node['unit'])
#     #     print(node['ifshowcode'])
#     #     print(node['dotcount'])
#     #     print(node['name'])
#     #     print(node['memo'])
#     #     print(node['cname'])
#     #     print(node['code'])
# for datanode in data['datanodes']:
#     print(datanode['code'])
#     print(datanode['wds'])
#     print(datanode['data'])
#
# #print(wdnodes)
# # for fl in zbfl.find({"data":{"$exists":"true"}}):
# #     print(fl)
# #     uid = str(fl['_id'])
# #     url = fl['urlnext']
# #     name = fl['name']
# #     pid = fl['pid']
# #     dbcode = fl['dbcode']
# #     wdcode = fl['wdcode']
# #     id = fl['id']
# #     isParent = fl['isParent']
# #     conn.execute("INSERT INTO zbfl(id,name,url,pid,dbcode,wdcode,uid,isParent) VALUES (?,?,?,?,?,?,?,?)",(id,name,url,pid,dbcode,wdcode,uid,isParent))
# #     conn.commit()
# # conn.close()
