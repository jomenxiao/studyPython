#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import sys


def get_all_flow(info_date):
	back_info = {}
	data = []
	url = 'http://%s' % info_date
	###url = [{},{}]
	response = urllib2.urlopen(url)
	response_json = json.loads(response.read())
	if "data" in response_json:

		# #name = list(set([ x["coa_name"] for x in response_json["data"] ]))
		# name = []
		# for x in response_json["data"]:
		# 	if x["coa_name"] not in name:
		# 		name.append(x["coa_name"])

		# for e_name in name:
		# 	e_info = {}
		# 	#print "e_name", e_name.encode("utf-8")
			
		# 	e_info["detail"] = [ x for x in response_json["data"] if x["coa_name"] == e_name ]
		# 	e_info["coa_name"] = e_name
		# 	e_info["peak"] = 0
		# 	e_info["peak_avg"] = 0
		# 	for e in e_info["detail"]:
		# 		#print e["coa_name"].encode("utf-8")
		# 		#e_info["ods_name"] = e["ods_name"]
		# 		e_info["peak"] += float(e["peak"])
		# 		e_info["peak_avg"] += float(e["peak_avg"])
			
		# 	data.append(e_info)
		# 	#print "ok"
		back_info = {"result":"right","data":response_json["data"]}
	else:
		back_info = {"result":"error"}

	return back_info

if __name__ == '__main__':
	print get_all_flow('2014_02_16')
	#print get_all_flow('2014_08_04')["data"][6]
	#print get_all_flow('2014_08_04')["data"][6]["coa_name"].encode('utf-8')

		