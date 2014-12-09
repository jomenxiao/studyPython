#!/usr/bin/env python
# -*- coding: utf-8 -*-
import get_flow
import write_mongo
import hand_info
import resource_info
import sys

def handle_date_info():
	date_info = resource_info.date_get_info()
	
	for e_date in date_info:
		insert_info = {}
		webgame_insert_info = {}
		#get every day flow
		#name_flow_list = {"result":"right","data":data}
		name_flow_list = get_flow.get_all_flow(e_date)
		if name_flow_list["result"] == "right":
			name_flow_list = name_flow_list["data"]
		else:
			print "NO RECORED"
			continue

		insert_info["date"] = e_date
		insert_info["data"] = hand_info.handle_name_cc_info(e_date,name_flow_list)

		webgame_insert_info["date"] = e_date
		webgame_insert_info["data"] = hand_info.handle_webgame_name_cc_info(e_date,name_flow_list)

		#print insert_info
		write_mongo.wirte_info(insert_info)
		write_mongo.webgame_wirte_info(webgame_insert_info)


def main():
	handle_date_info()



if __name__ == '__main__':
	main()