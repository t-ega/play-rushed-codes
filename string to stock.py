# tasks 2 Convert STRING TO STOCK PRICE DICTIONARY
stock_dict1 = {'SNAP': ['SNAP', 10.00], 'PINS': ['PINTEREST', 29.40], 'GOOG': ['Google', 96.50]}
# NOTE FOR THIS PROJECT YOU WOULD NEED A COMPREHENSIVE UNDERSTANDING OF HOW DICTIONARIES AND LISTS WORK IN PYTHON


def string_to_stock_dict(string) -> dict:
    # split the string when ever there is a space
    stock = string.split(' ')
    # make a for loop to access all the stocks
    for stocks in stock:
        # split the stock whenever there is a colon(:)
        stock = stocks.split(':')
        # make the list corresponding to the key i.e ['SNAP', 10.00], e.t.c
        stock_list = [stock[1], int(stock[2])]
        # add the items gotten to the dictionary
        stock_dict1.update({stock[0]: stock_list})
    return stock_dict1


# TESTING IF MY CODE ACTUALLY RUNS

print('Before ', stock_dict1)
string_to_stock_dict('Appl:app:280 chrm:chrome:590')
print('After ', stock_dict1)
