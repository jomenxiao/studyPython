#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import resource_info

def from_mongo_pcu(info_day,info_cc):
	data = {
		"bizid": info_cc,
		"datatype": "pcu",
		"params": {
		      "dt_start":  info_day + " 00:00:00",
		      "dt_end":  info_day + " 23:59:59",
		      "detail": 0,
		}
	}

	try:
		req = urllib2.Request('http://')
		req.add_header('Content-Type','application/json')

		response = urllib2.urlopen(req,json.dumps(data))
		response_json = json.loads(response.read())
		#print response_json
		back_info = max(response_json, key=lambda x:int(x["count"]))

		if "count" not in back_info:
			back_info = {"result":"error"}
		else:
			back_info = {"result":"right","data":back_info}

	except:
		back_info = {"result":"error"}
	#print back_info
	return back_info

if __name__ == '__main__':
	print from_mongo_pcu("2014-07-30",127)
	# for e in resource_info.webgame_name_cc_info():
	# 	#print from_mongo_pcu("2014-07-30",int(e["cc_id"]))
	# 	print e
	# 	print from_mongo_pcu("2014-07-30",int(e["cc_id"]))