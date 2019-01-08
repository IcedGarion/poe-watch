# python3

import requests, os, sys, time, pyperclip
from bs4 import BeautifulSoup

if __name__ == "__main__":
	# CONFIGURATIONS
	config_filename = "config.txt"
	config = { line.split('=')[0]: line.split('=')[1] for line in open(config_filename).read().split(os.linesep) if len(line) != 0 }

	items_file = config["items_file"]
	currencies = ['chaos', 'exalted']

	# reads from items list file: url and currency
	#custom_items = [ (line.split(' ')[0], line.split(' ')[1:3]) for line in open(items_filename).read().split(os.linesep) if len(line) != 0 ]
	custom_items = [ (line.split(' ')[0], line.split(' ')[1:3]) for line in open(items_file).read().split(config["linesep"]) if len(line) != 0 ]

	# LOOP
	n = 0
	while True:
		# output feedback
		if n == 1:
			sys.stdout.write("Searching...")
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
					# ITEM FOUND: builds message
					try:
						message = '@'+item.get('data-ign') + ' Hi, I would like to buy your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' in ' + item.get('data-league')+' (stash tab \"' + item.get('data-tab')+ '\"; position: left ' + item.get('data-x')+ ', top ' +item.get('data-y') +')'
					except TypeError:
						message = '@'+item.get('data-ign') + ' Hi, I would like to buy your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' in ' + item.get('data-league')
					# copy message to clipboard & writes to out_file
					pyperclip.copy(message)
					open(config["out_file"], 'a').write(item_name + " (" + item.get('data-buyout') + ")" + os.linesep + poe_trade_url + \
						os.linesep + message + os.linesep)
					sys.stdout.write('='*80 + os.linesep + item.get('data-buyout') + ": " + item_name + " (@" + item.get('data-ign') + ")" \
						+ os.linesep + "(Message copied to clipboard. Or see " + config["out_file"]  + ")" + os.linesep + '='*80 + os.linesep + os.linesep)
					custom_items.remove(item_data)
					n = 0
					break

		n += 1
		time.sleep(float(config["update_freq"]))
