###############################################################################
# Programmer: Stephen Yoder
# Developed for Flexera Assessment
###############################################################################

###############################################################################
# Class Stock_Profit
# The Stock_Profit class is designed to store stock data in chronological order

#  Inputs:
#   stock_prices: List[float] representing the intraday stock price in chronological order.
#                 The minimum value of an element in stock_prices is 0
###############################################################################
class Stock_Profit:
    def __init__(self, stock_prices):

        # List to hold the stock prices for the day in increasing chronological time order
        self.stock_prices = []
        for price in stock_prices:
            if price < 0:
                raise ValueError("negative stock price")
            self.stock_prices.append(price)

    #####################################################
    # calculate_max_profit:
    #  the max profit is found by finding the largest difference
    #  between the current price of the stock and the lowest
    #  price of the stock from earlier in the day
    #
    # Algorithm:
    #  Iterate through the stock prices, keep track of the
    #  lowest price seen so far. Calculate the difference
    #  between the lowest price and the current prices.
    #  Update max_profit if greater than the current
    #  max_profit
    #
    # Time Complexity: O(n)
    #
    # Inputs:
    #   None
    # Outputs:
    #   max_profit: float representing the maximum profit
    #               that can be obtained by making one buy and sell
    #               of the stock during the day
    #####################################################
    def calculate_max_profit(self):
        max_profit = 0
        lowest_price = float('inf') # lowest price for the stock that has been seen so far

        for price in self.stock_prices:
            lowest_price = min(lowest_price, price)
            max_profit = max(max_profit, price - lowest_price)

        return max_profit