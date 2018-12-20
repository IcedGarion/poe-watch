# DESCRIPTION
This application tracks if there are discounts on poe.trade.
It continuously searches poe.trade for the items you are interested in, reading from the items list;
it checks whether the items' prices are below the specified ones, and notify you if there is a match.

Only works for uniques items (for now).


# SETUP & RUN
- put some URLs in items_list.txt file:
	Example (Inpulsa's broken heart)
	http://poe.trade/search/ihohametootono

- define a price threshold for every item (next to its URL):
	Example:
	http://poe.trade/search/ihohametootono 10 chaos

	(currency names are 'chaos', 'exalted';
	you can add comments after the price)

- run:
	python3 poe_watch.py

- wait for output (for now)


# TODO
- read from file and save urls (repeat processing for every url) and associated thresholds

- check notify code

- conversion functions for popular currencies (chaos to ex and vice)
