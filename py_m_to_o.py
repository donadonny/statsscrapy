'''将清洗后的在mongodb中的数据转存到oracle中'''
import pymongo
import json
import cx_Oracle
from pymongo import MongoClient
con = cx_Oracle.connect('stats/stats@localhost/orcl')
cur = con.cursor()
client = MongoClient('localhost', 27017)
db = client.stats
indifl = db.indi_fl
indi = db.indi
indidata = db.indi_data
def insertzbfl():
	m=[]
	for data in indifl.find({}):
		dbcode = data['dbcode']
		id = data['id']
		cname = data['name']
		isParent = data['isParent']
		pid = data['pid']
		m.append((dbcode,id,cname,isParent,pid))
	# for x in range(1,len(m)):
	# 	print(m[x])
	cur.executemany("INSERT INTO zbfl(dbcode,id,cname,isParent,pid) VALUES (:1,:2,:3,:4,:5)",m)
	cur.execute('commit')
	cur.close
	con.commit
	con.close
	print("zbdl done")
def insertzb():
	m=[]
	for data in indi.find({}):
		dbcode = "hgyd"
		code = data['code']
		cname = data['name']
		cnamef = data['cname']
		exp = data['exp']
		memo = data['memo']
		unit = data['unit']
		dotcount =data['dotcount']
		m.append((dbcode,code,cname,cnamef,exp,memo,unit,dotcount))
	# for x in range(1,len(m)):
	# 	print(m[x])
	cur.executemany("INSERT INTO zb(dbcode,code,cname,cnamef,exp,memo,unit,dotcount) VALUES (:1,:2,:3,:4,:5,:6,:7,:8)",m)
	cur.execute('commit')
	cur.close
	con.commit
	con.close
	print("zb done")
def insertzbdata():
	m=[]
	for data in indidata.find({}):
		dbcode = "hgyd"
		zdcode = data['zbcode']
		sj = data['sj']
		dq = data['dq']
		strdata = data['strdata']
		m.append((dbcode,zdcode,sj,dq,strdata))
	# for x in range(1,len(m)):
	# 	print(m[x])
	cur.executemany("INSERT INTO zbdata(dbcode,zdcode,sj,dq,strdata) VALUES (:1,:2,:3,:4,:5)",m)
	cur.execute('commit')
	cur.close
	con.commit
	con.close
	print("zbdata done")
insertzbfl()
insertzb()
insertzbdata()
