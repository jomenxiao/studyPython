#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

db_name = "cdn_info"
db_host = "127.0.0.1"
db_port = 27017
collection_cdn = "cdn_record"
webgame_collection_cdn = "webgame_cdn_record"
db_user = "test"
db_passwd = "1234"

conn=pymongo.Connection(host=db_host,port=db_port)
conn[db_name].authenticate(db_user,db_passwd)

db = conn[db_name]

def wirte_info(insert_info):
	db_collection_cdn = db[collection_cdn]

	sum_record = list(db_collection_cdn.find({"date":insert_info["date"]}))
	if len(sum_record) <= 1:
		db_collection_cdn.update({"date":insert_info["date"]},
								 {"$set":{"data":insert_info["data"]}},
								 upsert=True)
	else:
		print "mongodb have ",sum_record,"record"
	return 

def webgame_wirte_info(insert_info):
	db_collection_cdn = db[webgame_collection_cdn]

	sum_record = list(db_collection_cdn.find({"date":insert_info["date"]}))
	if len(sum_record) <= 1:
		db_collection_cdn.update({"date":insert_info["date"]},
								 {"$set":{"data":insert_info["data"]}},
								 upsert=True)
	else:
		print "mongodb have ",sum_record,"record"
	return 

if __name__ == '__main__':
	wirte_info({"date":"2014-06-10","data":"data123"})