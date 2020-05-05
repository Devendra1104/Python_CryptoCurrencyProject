import requests
import json

def get_bitcoin_ethereum(cryp_curr,currency):
 	# url = 'https://api.coindesk.com/v1/bpi/currentprice/'+currency+'.json'
 	url = 'https://min-api.cryptocompare.com/data/price?fsym='+cryp_curr+'&tsyms='+currency
 	#print(url)
 	response = requests.get(url)
 	#print(response,response.text, type(response.text))
 	j_response = json.loads(response.text)
 	#print(j_response,type(j_response))
 	price = str(j_response[currency])
 	return price
print("USD rate for ethereum: $"+get_bitcoin_ethereum('ETH','USD')+ " and INR rate for ethereum: ₹" +get_bitcoin_ethereum('ETH','INR'))
# print()
print("USD rate for Bitcoin: $"+get_bitcoin_ethereum('BTC','USD')+ " and INR rate is for Bitcoin: ₹" +get_bitcoin_ethereum('BTC','INR'))
# print()

