# Programmer: Stephen Yoder
# Developed for Flexera Assessment
# Q2. You are tasked to study historic stock market performance.
# You are given an array N of intraday stock prices containing n elements.
# The profit/loss that can be made buying a stock at time i and selling it
# at later time j can be expressed by (N[j] - N[i]), j > i. Write a time/size
# efficient algorithm to calculate the maximum profit that can be made
# buying and selling a stock in a single day given N.

class Stock:
    def __init__(self, stock_prices):
        # List to hold the stock prices for the day in increasing time order
        self.stock_prices = stock_prices

    #####################################################
    # max profit is found by finding the largest difference
    # between the current price of the stock and the lowest
    # price of the stock from earlier in the day
    #
    # Algorithm:
    #  Iterate through the stock prices, keep track of the
    #  lowest price seen so far. Calculate the difference
    #  between the lowest price and the current prices.
    #  Update max_profit if greater than the current
    #  max_profit
    #####################################################
    def calculate_max_profit(self):
        max_profit = 0
        lowest_price = float('inf') # lowest price for the stock that has been seen so far

        for price in self.stock_prices:
            lowest_price = min(lowest_price, price)
            current_profit = price - lowest_price
            max_profit = max(max_profit, current_profit)

        return max_profit