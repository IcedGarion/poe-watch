# python3

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
	# reads from items list file: url and currency

	custom_value = 10
	custom_currency = "exalted"




	# currencies (ordered by value)
	currencies = ['chaos', 'exalted']


	# to be removed
	example = "http://poe.trade/search/ihohametootono"
	poe_trade_url = example

	# http get
	r = requests.get(poe_trade_url, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	# html parse
	soup = BeautifulSoup(r.text, 'html.parser')
	items = soup.find_all("tbody", { "class" : "item" })

	for item in items:
		#pyperclip.copy('@'+item.get('data-ign') + ' Hi, I would like to buy your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' in ' + item.get('data-league')+' (stash tab \"' + item.get('data-tab')+ '\"; position: left ' + item.get('data-x')+ ', top ' +item.get('data-y') +')')
		actual_value = item.get('data-buyout')
		actual_currency = actual_value.split(' ')[1].lower()
		actual_value = float(actual_value.split(' ')[0])

		# notifies only if currency type is less valuable of that specified, or equals (but less quantity)
		if currencies.index(actual_currency) < currencies.index(custom_currency) \
		or currencies.index(actual_currency) == currencies.index(custom_currency) and actual_value <= custom_value:
			print(item.get('data-buyout') + ": " + item.get('data-name') + " (@" + item.get('data-ign') + ")")
