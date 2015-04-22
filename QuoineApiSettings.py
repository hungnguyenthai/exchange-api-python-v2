#! /usr/bin/python

class Settings():

   	UserAgent  = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"
	UserId     = "59"
	ContentType= "application/json"
        UserSecret = "ASECRETCODETOBEUPDATEDFROMUSERSETTIMGSPAGE=="
	Headers = {
   		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0",
		"X-Quoine-Device": DeviceName,
   		"X-Quoine-User-Id":UserId,
   		"X-Quoine-User-Token": UserToken
  	}

	# Base URL for API calls
	BaseURL = "https://api.quoine.com"

	# URI parts for calling API - to be added to BaseURL per call
	GetAccountsURI    = "/accounts"				# [GET] 				
	GetOrderURI       = "/orders/%s"			# [GET] 				
	GetOrdersURI      = "/orders?currency_pair_code=%s%s"	# [GET] 				
	GetProductURI     = "/products/code/%s/%s"              # [GET] 				
	GetProductsURI    = "/products"				# [GET] 				
        GetPriceLadderURI = "/products/%s/price_levels"         # [GET]
        AddOrderURI       = "/orders"                           # [POST]
	CancelOrderURI    = "/orders/%s/cancel"	        	# [PUT]

if __name__ == "__main__":
  gbl = Settings()
  print gbl.UserAgent
  print gbl.UserId
  print gbl.DeviceName
  print gbl.UserToken
