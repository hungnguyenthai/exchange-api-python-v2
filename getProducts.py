#! /usr/bin/python
import os
import sys
import json
import requests
from QuoineApiSettings import Settings

api = Settings()

url = api.BaseURL + api.GetProductsURI

if len(sys.argv) > 1:
  url = "%s/%s" % (url, sys.argv[1])
r = requests.get(url)
if r.status_code == 200:
   if r.text == "null":
      print "No content returned for URL %s" % url
   else:
      data = json.loads(r.text)
      for ccy in data:
         print "\n\n"
         print ccy
else:
   print "\nError %s while calling URL %s:\n" % (r.status_code,url)
