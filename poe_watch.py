# python3

import requests, os, sys
from bs4 import BeautifulSoup

if __name__ == "__main__":
	items_filename = "items_list.txt"
	currencies = ['chaos', 'exalted']

	# reads from items list file: url and currency
	custom_items = [ (line.split(' ')[0], line.split(' ')[1:3]) for line in open(items_filename).read().split(os.linesep) if len(line) != 0 ]

	# LOOP
	n = 0
	while True:
		# output feedback
		if n == 1:
			sys.stdout.write("Keep searching...")
		elif n > 1 and n%2 == 0:
			sys.stdout.write('.')
		sys.stdout.flush()

		# poe.trade search for every item in the list
		for item_data in custom_items:
			poe_trade_url = item_data[0]
			custom_value = float(item_data[1][0])
			custom_currency = item_data[1][1]

			if n == 0:
				sys.stdout.write("Connecting to " + poe_trade_url + "... ")

			# http get
			r = requests.get(poe_trade_url, headers={'Content-Type': 'application/x-www-form-urlencoded'})
			# html parse
			soup = BeautifulSoup(r.text, 'html.parser')
			poe_trade_items = soup.find_all("tbody", { "class" : "item" })
			item_name = ""

			# for every item in poe.trade, price check
			for i, item in enumerate(poe_trade_items):
				#pyperclip.copy('@'+item.get('data-ign') + ' Hi, I would like to buy your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' in ' + item.get('data-league')+' (stash tab \"' + item.get('data-tab')+ '\"; position: left ' + item.get('data-x')+ ', top ' +item.get('data-y') +')')
				actual_value = item.get('data-buyout')
				actual_currency = actual_value.split(' ')[1].lower()
				actual_value = float(actual_value.split(' ')[0])
				item_name = item.get('data-name')

				# output feedback
				if i == 0 and n == 0:
					sys.stdout.write("( " + item_name + " )" + os.linesep)
					sys.stdout.flush()

				# notifies only if currency type is less valuable of that specified, or equals (but less quantity)
				if currencies.index(actual_currency) < currencies.index(custom_currency) \
				or currencies.index(actual_currency) == currencies.index(custom_currency) and actual_value <= custom_value:
					sys.stdout.write(os.linesep + item.get('data-buyout') + ": " + item_name + " (@" + item.get('data-ign') + ")" + os.linesep)
					n = 0
					custom_items.remove(item_data)
					break

		n += 1
