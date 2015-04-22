#! /usr/bin/python
import os
import sys
import requests
import hashlib
import hmac
import json
import md5
import base64
import uuid
from QuoineApiSettings import Settings
from QuoineApiUtility import TimestampGMT, GetAPIKey

ccy_list = ["AUD","IDR","HKD","SGD","JPY","PHP","USD"]
if len(sys.argv) > 1:
  currency = sys.argv[1]
else:
  print "No Currency provided - must be one of %s" % ', '.join(ccy_list)
  sys.exit(1)

if currency not in ccy_list:
  print "Invalid currency '%s' - must be one of %s " % (currency, ', '.join(ccy_list))
  sys.exit(1)

base_currency = "BTC"

api = Settings()
user_agent = api.UserAgent
data = ""
ctype = api.ContentType
cMD5 = base64.b64encode(md5.new(data).digest())
print "MD5 :" +  cMD5

nonce = str(uuid.uuid4()).upper().replace("-","")[0:32]
print "Nonce : " + nonce + " " + str(len(nonce))

uri = api.GetOrdersURI % (base_currency,currency)
theDate = TimestampGMT()

cstr = "%s,%s,%s,%s,%s" % (ctype,cMD5,uri,theDate,nonce)
print "Canonical String :" + cstr

key = api.UserSecret
print "API Secret : " + key

hash = hmac.new(bytes(key), bytes(cstr),hashlib.sha1).digest()
print "B64 HASH : " + base64.encodestring(hash)

auth_str = "%s %s:%s" % ('APIAuth', api.UserId, base64.b64encode(hash))
print "Authorization : " + auth_str

hdrs = {'User-Agent' : api.UserAgent,'NONCE': nonce,'Date': theDate, 'Content-Type': api.ContentType, 'Content-MD5': cMD5,  'Authorization': auth_str }

url = api.BaseURL + uri
print "URL : ", url
try:
  r = requests.get(url,headers=hdrs)
  print r.status_code
  data = json.loads(r.text)
  for order in data["models"]:
    print "\n================================="
    print order["id"], " ", order["status"]," ",order["price"], " ", order["quantity"]
except requests.exceptions.HTTPError as e:
  print "Error: \n"
  print e
