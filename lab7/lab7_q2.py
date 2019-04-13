class Stock:

    # contructor has 4 private data fields, prices default to 0
    def __init__(self, symbol, name, previous_closing_price = 0, current_price = 0):
        self.__symbol = symbol
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price

    # method for returning stock name
    def get_stock_name(self):
        return self.__name

    # method for returning stock symbol
    def get_stock_symbol(self):
        return self.__symbol

    # method for returning previous price
    def get_previous_price(self):
        return self.__previous_closing_price

    # method to set the previous price
    def set_previous_price(self, previous_closing_price):
        self.__previous_closing_price = previous_closing_price

    # method to return current price
    def get_current_price(self):
        return self.__current_price

    # method to set current price
    def set_current_price(self, current_price):
        self.__current_price = current_price

    # method to calculate the change percentage
    # I don't multiply by 100, since format() will by using %
    def get_change_percent(self):
        return format((self.__current_price - self.__previous_closing_price)\
        / self.__previous_closing_price, ".2%")


def main():
    # instantiate stock object, give symbol and name
    stock = Stock("INTC", "Intel Corporation")
    # set the respective prices
    stock.set_previous_price(20.5)
    stock.set_current_price(20.35)
    # print the results
    print("Stock:", stock.get_stock_symbol(), stock.get_stock_name())
    print("Previous Closing Price:", stock.get_previous_price())
    print("Current Price:", stock.get_current_price())
    print("Price Change Percentage:", stock.get_change_percent())

main()

"""
Stock: INTC Intel Corporation
Previous Closing Price: 20.5
Current Price: 20.35
Price Change Percentage: -0.73%
"""
