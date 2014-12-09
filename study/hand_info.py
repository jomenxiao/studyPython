#!/usr/bin/env python
# -*- coding: utf-8 -*-

import get_pcu
import resource_info


# def handle_name_cc_info(e_date,name_flow_list):
# 	name_cc_id = resource_info.name_cc_info()
# 	e_data = {}
# 	for e_cc_id in name_cc_id:
# 		e_id = e_cc_id["cc_id"]
# 		e_name = e_cc_id["name"]		
# 		e_info =  {}
# 		#get pcu and pcu timestamp
# 		pcu_info = get_pcu.from_mongo_pcu(e_date,e_id)
# 		if pcu_info["result"] == "right":
# 			pcu_info = pcu_info["data"]
# 			pcu_online = int(pcu_info["count"])
# 			pcu_datetime = pcu_info["dtEventTime"]
# 			for e_flow in name_flow_list:
# 				if e_name == e_flow["coa_name"]:
# 					app_detail = e_flow["detail"]
# 					#print app_detail
# 					e_peak = round(e_flow["peak"] * 1024 * 1024, 5)
# 					if pcu_online == 0:
# 						e_online_flow_avg = -1
# 					else:
# 						e_online_flow_avg = round( e_peak / pcu_online, 5)

# 					e_peak_avg = round(e_flow["peak_avg"] * 1024 * 1024, 5)

# 					#e_info["test_name"] = test_name
# 					e_info["name"] = e_flow["coa_name"]				
# 					e_info["peak"] = e_peak
# 					e_info["peak_avg"] = e_peak_avg
# 					e_info["cc_id"] = e_id
# 					e_info["timestamp"] = pcu_datetime
# 					e_info["online"] = pcu_online
# 					e_info["online_flow_avg"] = e_online_flow_avg
# 					e_info["detail"] =  app_detail

# 		e_data[str(e_id)] = e_info

# 	return e_data

def handle_name_cc_info(e_date,name_flow_list):
	name_cc_id = resource_info.name_cc_info()
	e_data = {}	
	for e_flow in name_flow_list:

		for e_cc_id in name_cc_id:
			e_id = e_cc_id["cc_id"]
			e_name = e_cc_id["name"]	

			if e_name == e_flow["coa_name"] or e_name == e_flow["test_name"]	 or e_name == e_flow["bu_name"] :							
				if str(e_id) in e_data:
					e_info = e_data[str(e_id)]
					e_info["test_record"] = e_info["test_record"] + 1
					e_info["peak"] = round((e_info["peak"] + float(e_flow["peak"]) * 1024 * 1024) / e_info["test_record"], 5)
					e_info["peak_avg"] = round((e_info["peak_avg"] + float(e_flow["peak_avg"]) * 1024 * 1024) / e_info["test_record"], 5)					

				else:
					e_info = {}
					e_info["detail"] = []
					e_info["all_name"] = []
					e_info["cc_id"] = e_id
					e_info["name"] = e_name

					e_info["test_record"] = 1
					e_info["peak"] =  float(e_flow["peak"]) * 1024 * 1024
					e_info["peak_avg"] =  float(e_flow["peak_avg"]) * 1024 * 1024
					#handle online info
					pcu_info = get_pcu.from_mongo_pcu(e_date,e_id)
					if pcu_info["result"] == "right":
						pcu_info = pcu_info["data"]
						e_info["online"] = int(pcu_info["count"])
						e_info["timestamp"] = pcu_info["dtEventTime"]
					else:
						e_info["online"] = 0
						e_info["timestamp"] = "NULL"
						e_info["online_flow_avg"] = 0					
				
				if e_info["online"] != 0:
					e_info["online_flow_avg"] = round(e_info["peak"] / e_info["online"], 5)
				else:
					e_info["online_flow_avg"] = 0

				e_info["detail"].append(e_flow)					

				if e_flow["coa_name"] not in e_info["all_name"]:
					e_info["all_name"].append(e_flow["coa_name"])
				if e_flow["test_name"] not in e_info["all_name"]:
					e_info["all_name"].append(e_flow["test_name"])						
				if e_flow["bu_name"] not in e_info["all_name"]:
					e_info["all_name"].append(e_flow["bu_name"])
				#print e_info
				e_data[str(e_id)] = e_info

	return 	e_data


def handle_webgame_name_cc_info(e_date,name_flow_list):
	name_cc_id = resource_info.webgame_name_cc_info()
	e_data = {}	
	for e_flow in name_flow_list:

		for e_cc_id in name_cc_id:
			e_id = e_cc_id["cc_id"]
			e_name = e_cc_id["name"]
			e_test_name = e_cc_id["test_name"]	

			if e_flow["test_name"] in e_test_name :							
				if str(e_id) in e_data:
					e_info = e_data[str(e_id)]
					e_info["test_record"] = e_info["test_record"] + 1
					e_info["peak"] = round((e_info["peak"] + float(e_flow["peak"]) * 1024 * 1024) / e_info["test_record"], 5)
					e_info["peak_avg"] = round((e_info["peak_avg"] + float(e_flow["peak_avg"]) * 1024 * 1024) / e_info["test_record"], 5)					

				else:
					e_info = {}
					e_info["detail"] = []
					e_info["all_name"] = []
					e_info["cc_id"] = e_id
					e_info["name"] = e_name

					e_info["test_record"] = 1
					e_info["peak"] =  float(e_flow["peak"]) * 1024 * 1024
					e_info["peak_avg"] =  float(e_flow["peak_avg"]) * 1024 * 1024
					#handle online info
					pcu_info = get_pcu.from_mongo_pcu(e_date,e_id)
					if pcu_info["result"] == "right":
						pcu_info = pcu_info["data"]
						e_info["online"] = int(pcu_info["count"])
						e_info["timestamp"] = pcu_info["dtEventTime"]
					else:
						e_info["online"] = 0
						e_info["timestamp"] = "NULL"
						e_info["online_flow_avg"] = 0					
				
				if e_info["online"] != 0:
					e_info["online_flow_avg"] = round(e_info["peak"] / e_info["online"], 5)
				else:
					e_info["online_flow_avg"] = 0

				e_info["detail"].append(e_flow)					

				if e_flow["coa_name"] not in e_info["all_name"]:
					e_info["all_name"].append(e_flow["coa_name"])
				if e_flow["test_name"] not in e_info["all_name"]:
					e_info["all_name"].append(e_flow["test_name"])						
				if e_flow["bu_name"] not in e_info["all_name"]:
					e_info["all_name"].append(e_flow["bu_name"])
				#print e_info
				e_data[str(e_id)] = e_info

	return 	e_data