#! /usr/bin/python
import os
import sys
import requests
import hashlib
import hmac
import md5
import base64
import uuid
from QuoineApiSettings import Settings
from QuoineApiUtility import TimestampGMT, GetAPIKey

order_id = 0
if len(sys.argv) > 1:
  try: 
    order_id = int(sys.argv[1])
  except ValueError:
    print "Invalid Id '%s' provided " % sys.argv[1]
    sys.exit(1)
else:
  print "No Order Id provided "
  sys.exit(1)

api = Settings()
user_agent = api.UserAgent
data = ""
ctype = api.ContentType
cMD5 = base64.b64encode(md5.new(data).digest())
print "MD5 :" +  cMD5

nonce = str(uuid.uuid4()).upper().replace("-","")[0:32]
print "Nonce : " + nonce + " " + str(len(nonce))

uri = api.CancelOrderURI % order_id
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

url = api.BaseURL  + uri
print "URL : ",url

try:
   response = requests.put(url,headers=hdrs)
   print response.status_code
   print response.text

except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
