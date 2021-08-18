###############################################################################
# Programmer: Stephen Yoder
# Developed for Flexera Assessment
###############################################################################
import heapq

###############################################################################
# Class Stock
# The Stock class is designed to store stock data

#  Inputs:
#   stock_prices: List[float] representing the intraday stock price in chronological order.
#                 The minimum value of an element in stock_prices is 0
###############################################################################
class Stock:
    def __init__(self, stock_prices):

        # List to hold the stock prices for the day in increasing chronological time order
        self.stock_prices = []
        for price in stock_prices:
            if price < 0:
                raise ValueError("negative stock price")
            self.stock_prices.append(price)

    #####################################################
    # max_profit:
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

    #####################################################
    # calculate_kth_highest_price:
    #  function to find the kth largest price seen that day
    #
    # Algorithm:
    #  Iterate through the stock prices and add that price
    #  to a heapq.
    #  The heapq data structure is structured as a binary
    #  tree and is thus similar to using a
    #  binary search and takes O(logn) time for retrieving
    #  an element. It is superiorto just sorting the
    #  input list of prices because sorting has O(nlogn)
    #  time complexity whereas using a heap has O(klogn)
    #  time complexity where it is guaranteed k <= n
    #
    # Time Complexity: O(klogn)
    #
    # Inputs:
    #   k: integer representing the kth highest stock price
    #      seen during the day.
    #      The minimum value is 1 and the maximum value is
    #      n, the number of values the stock had during the day
    # Outputs:
    #   nlargest: float representing the value of the stock
    #             at its kth highest value during the day
    #####################################################
    def calculate_kth_highest_price(self, k):

        if not self.stock_prices or k not in range(1, len(self.stock_prices)+1):
            return -1

        stock_prices_heapq = self.stock_prices[:] # deep copy so self.stock_prices is not converted to a heapq
        heapq.heapify(stock_prices_heapq) # heapq to store the prices for the day

        return heapq.nlargest(k, stock_prices_heapq)[-1]