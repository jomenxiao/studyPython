#!/bin/python
#coding=utf8

import os
import sys
import re
import codecs
import urllib
import BeautifulSoup

URL = "http://www.ip138.com/ips138.asp?ip="


def  getIpHtml(ip):
	htmlData = urllib.urlopen( URL + ip ).read().decode('gb2312')
	soup = BeautifulSoup.BeautifulSoup(htmlData)
	#print soup.title+
	 
	soupData  =  soup.findAll('td', align="center")
	soupIp =  soupData[1]
 
	soupInfo = soupData[2].findAll('li')

	print soupIp.text.encode('utf8')
	print soupInfo[0].text.encode('utf8')
	print soupInfo[1].text.encode('utf8')
	
	#print center.findAll('li')
	#print '\n'.join(dir(center))
	 


def main():
	if len(sys.argv)==2:
		ip = sys.argv[1]
	else:
		ip = raw_input("please input IP:")
		#ip = '173.194.72.199'

	if not re.findall(r'\d+\.\d+\.+\d+\.\d+', ip):
		print "IP is ERROR" 
		exit()
	else:
		ipNumberList = ip.split('.')

		if int(ipNumberList[0]) == 0:
			print "IP first number is ERROR"

		for number in range(len(ipNumberList)):
			if ipNumberList[number] < 0 and ipNumberList[number] > 255:
				print "IP number is ERROR"
				exit()


	getIpHtml(ip)



if __name__ == '__main__':	
	main()