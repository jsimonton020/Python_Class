class Stock:
    def __init__(self, symbol, name, previous_closing_price, current_price):
        self.__symbol = symbol
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price

    def get_stock_name(self):
        return self.__name

    def get_stock_symbol(self):
        return self.__symbol

    def get_previous_price(self):
        return self.__previous_closing_price

    def set_previous_price(self):
        self.__previous_closing_price = previous_closing_price
        return previous_closing_price

    def get_current_price(self):
        return self.__current_price

    def set_current_price(self):
        self.__current_price = current_price
        return previous_closing_price

    def get_change_percent(self):
        return (self.__current_price - self.__previous_closing_price)\
        / self.__previous_closing_price * 100


def main():
    stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print("Stock:", stock.get_stock_symbol(), stock.get_stock_name())
    print("Previous Closing Price:", stock.get_previous_price())
    print("Current Price:", stock.get_current_price())
    print("Price Change Percentage:", format(stock.get_change_percent()))

main()
