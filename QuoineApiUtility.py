#! /usr/bin/python

import os, sys
import urllib
import urllib2
import hashlib
import hmac
import md5
import httplib
import base64
import datetime
import time
from calendar import weekday
from QuoineApiSettings import *

def TimestampGMT():
	now = time.gmtime()
	if (now.tm_sec < 10):
    		sec = "0%s" % now.tm_sec
  	else:
    		sec = now.tm_sec

	if (now.tm_min < 10):
    		min = "0%s" % now.tm_min
  	else:
    		min = now.tm_min

  	if (now.tm_hour < 10):
    		hr = "0%s" % now.tm_hour
  	else:
    		hr = now.tm_hour

	dd = weekday(now.tm_year,now.tm_mon,now.tm_mday)

	if dd   == 0:
	  dow = "Mon"
        elif dd == 1: 
	  dow = "Tue"
        elif dd == 2: 
	  dow = "Wed"
        elif dd == 3: 
	  dow = "Thu"
        elif dd == 4: 
	  dow = "Fri"
        elif dd == 5: 
	  dow = "Sat"
        elif dd == 6: 
	  dow = "Sun"

	if now.tm_mon  == 1:
	  mon = "Jan"
        elif now.tm_mon == 2: 
	  mon = "Feb"
        elif now.tm_mon == 3: 
	  mon = "Mar"
        elif now.tm_mon == 4: 
	  mon = "Apr"
        elif now.tm_mon == 5: 
	  mon = "May"
        elif now.tm_mon == 6: 
	  mon = "Jun"
        elif now.tm_mon == 7: 
	  mon = "Jul"
        elif now.tm_mon == 8: 
	  mon = "Aug"
        elif now.tm_mon == 9: 
	  mon = "Sep"
        elif now.tm_mon == 10: 
	  mon = "Oct"
        elif now.tm_mon == 11: 
	  mon = "Nov"
        elif now.tm_mon == 12: 
	  mon = "Dec"

   	dt = "%s, %s %s %s %s:%s:%s GMT" % (dow, now.tm_mday,mon,now.tm_year,hr,min,sec)
	return dt 

def GetAPIKey(): 

	gbl = Global()
	# get api secret key
	headers = {'User-Agent' : gbl.UserAgent, 'Content-Type': gbl.ContentType }
	data = '{"email": "tinwald@gmail.com","password": "Password88"}'

	url = gbl.BaseTestingURL + gbl.GetApiKeyURI
	req = urllib2.Request(url, data, headers)

	skey = ""

	try:
		pass
		#f = urllib2.urlopen(req)
    		#resp = f.read()
	except Exception as ex:
    		#prints the HTTP error code that was given
    		print ex
    		print ex.args
    		raise Exception(ex)

	resp = '{ "api_secret_key": "qweretrtytryuyuiyuo" }'
	# add debug, verbose options
	return resp

