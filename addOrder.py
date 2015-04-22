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

ccy_list = ["BTCAUD","BTCIDR","BTCHKD","BTCSGD","BTCJPY","BTCUSD","BTCPHP"]
product_list = ["CASH"]

order = {}
price = 0
quantity = 0
order_type = ""
side = ""
currency_pair_code = ""
product_code = ""

if len(sys.argv) < 7:
  print "Full set of Order details not provided, should be <price> <quantity> <side> <order type> <currency pair> <product> "
  sys.exit(1)

try: 
  price = float(sys.argv[1])
  if price <= 0:
     print "Invalid price '%s' - must be greater than zero " % sys.argv[1]
     sys.exit(1)
  else:
     order['price'] = price
except ValueError:
  print "Invalid price '%s' provided " % sys.argv[1]
  sys.exit(1)

try: 
  quantity = float(sys.argv[2])
  if quantity <= 0:
     print "Invalid quantity '%s' - must be greater than zero " % sys.argv[2]
     sys.exit(1)
  else:
     order['quantity'] = quantity
except ValueError:
  print "Invalid price '%s' provided " % sys.argv[2]
  sys.exit(1)

side = sys.argv[3]
if side.lower() <> "buy" and side.lower() <> "sell":
  print "Invalid order side '%s' provided - must be either 'buy' or 'sell' " % side
  sys.exit(1)
else:
  order['side'] = side

order_type  = sys.argv[4]
if order_type .lower() <> "limit" and order_type.lower() <> "market" and order_type.lower() <> 'range':
  print "Invalid order type '%s' provided - must be 'limit', 'market' or 'range' " % order_type 
  sys.exit(1)
else:
  order['order_type'] = order_type

currency_pair_code  = sys.argv[5]
if currency_pair_code.upper() not in ccy_list:
  print "Invalid currency pair '%s' provided - must be one of %s " % (currency_pair_code," , ".join(ccy_list)) 
  sys.exit(1)
else:
  order['currency_pair_code'] = currency_pair_code

product_code  = sys.argv[6]
if product_code.upper() not in product_list:
  print "Invalid product code '%s' provided - must be one of %s " % (product_code," , ".join(product_list)) 
  sys.exit(1)
else:
  order['product_code'] = product_code

api = Settings()
user_agent = api.UserAgent
data = str(order)
ctype = api.ContentType
cMD5 = base64.b64encode(md5.new(data).digest())
print "MD5 :" +  cMD5

nonce = str(uuid.uuid4()).upper().replace("-","")[0:32]
print "Nonce : " + nonce + " " + str(len(nonce))

uri = api.AddOrderURI
theDate = TimestampGMT()
cstr = "%s,,%s,%s,%s" % (ctype,uri,theDate,nonce)
print "Canonical String :" + cstr

key = api.UserSecret
print "API Secret : " + key

hash = hmac.new(bytes(key), bytes(cstr),hashlib.sha1).digest()
print "B64 HASH : " + base64.encodestring(hash)

auth_str = "%s %s:%s" % ('APIAuth', api.UserId, base64.b64encode(hash))
print "Authorization : " + auth_str

hdrs = {'User-Agent' : api.UserAgent,'NONCE': nonce,'Date': theDate, 'Content-Type': api.ContentType, 'Authorization': auth_str }

url = api.BaseURL  + uri
print "URL : ",url

request = {}
request['order'] = order
print order
try:
   response = requests.post(url,data=json.dumps(request),headers=hdrs)
   print response.status_code
   #print response.headers
   print response.text

except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
