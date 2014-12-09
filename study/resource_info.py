#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import time


def date_get_info():
	date_list = []
	today = datetime.date.today()
	for e in range(1,200):
		e_day = (today - datetime.timedelta(days=e)).strftime("%Y-%m-%d")
		date_list.append(e_day)
	#print date_list
	return date_list

def webgame_name_cc_info():
	webgame_name_cc_id = [
		{u"test":u"test",	u"test":106, u"test":[u"test"]},

	]

	return webgame_name_cc_id

def name_cc_info():

	name_cc_id=[
		{u"test":u"test"	,u"test":343},

	]
	return name_cc_id

if __name__ == '__main__':
	#name_cc_info()
	print date_get_info()
