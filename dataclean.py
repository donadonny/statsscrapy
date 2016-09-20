"""本程序的功能将mongodb中爬取的原始数据，清洗整理成结构化数据，并存储到sqlit中，清洗指标分类"""
import sqlite3
import pymongo
import json
conn = sqlite3.connect('test.db')
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.items
zbfl = db.zbfl
for fl in zbfl.find({"wdcode":"zb"}):
    uid = str(fl['_id'])
    url = fl['urlnext']
    name = fl['name']
    pid = fl['pid']
    dbcode = fl['dbcode']
    wdcode = fl['wdcode']
    id = fl['id']
    isParent = fl['isParent']
    #try:
    conn.execute("INSERT INTO zbfl(id,name,url,pid,dbcode,wdcode,uid,isParent) VALUES (?,?,?,?,?,?,?,?)",(id,name,url,pid,dbcode,wdcode,uid,isParent))
    conn.commit()
conn.close()















     #
# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
# conn.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print("Table created successfully")
# conn.close()