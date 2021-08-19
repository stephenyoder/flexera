###############################################################################
# Programmer: Stephen Yoder
# Developed for Flexera Assessment
###############################################################################
import heapq

###############################################################################
# Class kth_Highest_Stock_Price
# The kth_Highest_Stock_Price class is designed to store stock data in chronological order
#  A (min/max)heapq data structure is a binary heap used as a priority queue where the 0th
#  element is guarenteed to be the min/max value in the heapq. It provides O(logn) push and pop time
#
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

    #####################################################
    # calculate_kth_highest_price:
    #  function to find the kth largest price seen that day
    #
    # Algorithm:
    #  Use python's built in heapq function, nlargest()
    #  The
    #  It is superior to just sorting the
    #  input list of prices because sorting has O(nlogn)
    #  time complexity whereas using a heap has O(nlogk)
    #  time complexity for nlargest where it is guaranteed k <= n.
    #  However, creating the heapq solution requires O(k) space
    #  whereas sorting is done in place O(1)
    #
    # Time Complexity: O(nlogk)
    #
    # Inputs:
    #   k: integer representing the kth highest stock price
    #      seen during the day.
    #      The minimum value is 1 and the maximum value is
    #      n, the number of values the stock had during the day
    # Outputs:
    #   nlargest: float representing the value of the stock
    #             at its kth highest value during the day
    #             Returns -1 if there is no stock data or
    #             k is not in the valid range
    #####################################################
    def calculate_kth_highest_price(self, k):

        if not self.stock_prices or k not in range(1, len(self.stock_prices)+1):
            return -1

        return heapq.nlargest(k, self.stock_prices)[-1]