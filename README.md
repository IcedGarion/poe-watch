## DESCRIPTION

This application tracks if there are discounts on poe.trade.

It continuously searches poe.trade for the items you are interested in, reading from the items list;

it checks whether the items' prices are below the specified ones, and notify you if there is a match.



Only works for uniques items (for now).





## INSTALL


- Install python3:
  https://www.python.org/downloads/ (make sure to check "Add python3 to PATH")



- Install required python libraries:
  double-click install.bat




## SETUP & CONFIGURE

- put some URLs in items_list.txt file:

	Example (Inpulsa's broken heart)

	http://poe.trade/search/ihohametootono



- define a price threshold for every item (next to its URL):

	Example:

	http://poe.trade/search/ihohametootono 10 chaos



	(currency names are 'chaos', 'exalted';
	you can add comments after the price)




## RUN:
- Double click "run.bat"



# DETAILED DESCRIPTION
After you configured items_list.txt properly, launch the script and wait for it to find a discounted item.
If the program is stuck on 'Searching...' it means that there is no item match. Leave it in background and wait.
When an item is found, a text appears: the last buying message is copied to your clipboard and you can paste it (CTRL+V) in poe chat "@seller Hi, i would like to buy...".
You can even open messages.txt for a detailed response of all the results found. 

You can change the update frequency in config.txt: default is 0.5 (seconds).
If poe lags or you have network issues set it to, say, 10. It means that once every 10 seconds the script checks on poe.trade for the items you listed .




## TODO

- better notify system

- conversion functions for popular currencies (chaos to ex and vice)
