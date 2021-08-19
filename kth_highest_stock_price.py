###############################################################################
# Programmer: Stephen Yoder
# Developed for Flexera Assessment
###############################################################################
import heapq

###############################################################################
# Class Stock_Profit
# The Stock_Profit class is designed to store stock data in chronological order

#  Inputs:
#   stock_prices: List[float] representing the intraday stock price in chronological order.
#                 The minimum value of an element in stock_prices is 0
###############################################################################
class kth_Highest_Stock_Price:
    def __init__(self, stock_prices):

        # List to hold the stock prices for the day in increasing chronological time order
        self.stock_prices = []
        for price in stock_prices:
            if price < 0:
                raise ValueError("negative stock price")
            self.stock_prices.append(price)

        heapq.heapify(self.stock_prices)  # heapq to store the prices for the day

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

        return heapq.nlargest(k, self.stock_prices)[-1]