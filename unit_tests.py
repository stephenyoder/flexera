import unittest
from stock_profit import Stock_Profit
from room_reserve_api import Room_Reserve_API
from kth_highest_stock_price import kth_Highest_Stock_Price

test_cases = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
              [3, 3, 99, 100, 3985, 83, 9, 0, 39, 10, 5],
              [3, 2, 4, 5, 20, 0, 1000, 10001, 4, 5, 399],
              [1, 2, 3, 5, 99999, 999999],
              [4, 50034, 1, 400000, 3, 2, 4, 999],
              [1],
              [1, 2],
              [2, 1],
              [],
              [1, 1.2, 5.5, 3.4],
              [1, 2, 3.3, -0.0, 0.0],
              [9, 1, 1.2, 5.5, 3.4, 9.0]]

class Stock_Profit_Test(unittest.TestCase):
    def test_stock_profit(self):

        test0 = Stock_Profit(test_cases[0])
        test1 = Stock_Profit(test_cases[1])
        test2 = Stock_Profit(test_cases[2])
        test3 = Stock_Profit(test_cases[3])
        test4 = Stock_Profit(test_cases[4])
        test5 = Stock_Profit(test_cases[5])
        test6 = Stock_Profit(test_cases[6])
        test7 = Stock_Profit(test_cases[7])
        test8 = Stock_Profit(test_cases[8])
        test9 = Stock_Profit(test_cases[9])
        test10 = Stock_Profit(test_cases[10])
        test11 = Stock_Profit(test_cases[11])
        test12 = Stock_Profit(test_cases[12])
        self.assertRaises(ValueError, Stock_Profit, [-1, -2.3, 5, 0])
        self.assertRaises(ValueError, Stock_Profit, [0, 2, 5, 0, -3.3])

        self.assertEqual(test0.calculate_max_profit(), 9)
        self.assertEqual(test1.calculate_max_profit(), 0)
        self.assertEqual(test2.calculate_max_profit(), 3982)
        self.assertEqual(test3.calculate_max_profit(), 10001)
        self.assertEqual(test4.calculate_max_profit(), 999998)
        self.assertEqual(test5.calculate_max_profit(), 399999)
        self.assertEqual(test6.calculate_max_profit(), 0)
        self.assertEqual(test7.calculate_max_profit(), 1)
        self.assertEqual(test8.calculate_max_profit(), 0)
        self.assertEqual(test9.calculate_max_profit(), 0)
        self.assertEqual(test10.calculate_max_profit(), 4.5)
        self.assertEqual(test11.calculate_max_profit(), 2.3)
        self.assertEqual(test12.calculate_max_profit(), 8)

class kth_Highest_Stock_Price_Test(unittest.TestCase):
    def test_kth_Highest_Stock_Price(self):

        test0 = kth_Highest_Stock_Price(test_cases[0])
        test1 = kth_Highest_Stock_Price(test_cases[1])
        test2 = kth_Highest_Stock_Price(test_cases[2])
        test3 = kth_Highest_Stock_Price(test_cases[3])
        test4 = kth_Highest_Stock_Price(test_cases[4])
        test5 = kth_Highest_Stock_Price(test_cases[5])
        test6 = kth_Highest_Stock_Price(test_cases[6])
        test7 = kth_Highest_Stock_Price(test_cases[7])
        test8 = kth_Highest_Stock_Price(test_cases[8])
        test9 = kth_Highest_Stock_Price(test_cases[9])
        test10 = kth_Highest_Stock_Price(test_cases[10])
        test11 = kth_Highest_Stock_Price(test_cases[11])
        test12 = kth_Highest_Stock_Price(test_cases[12])
        self.assertRaises(ValueError, kth_Highest_Stock_Price, [-1, -2.3, 5, 0])
        self.assertRaises(ValueError, kth_Highest_Stock_Price, [0, 2, 5, 0, -3.3])

        for i in range(len(test_cases[0])+2):
            self.assertEqual(test0.calculate_kth_highest_price(i), sorted(test_cases[0], reverse=True)[i-1] if i in range(1, len(test_cases[0])+1) else -1)
        for i in range(len(test_cases[1])+2):
            self.assertEqual(test1.calculate_kth_highest_price(i), sorted(test_cases[1], reverse=True)[i-1] if i in range(1, len(test_cases[1])+1) else -1)
        for i in range(len(test_cases[2])+2):
            self.assertEqual(test2.calculate_kth_highest_price(i), sorted(test_cases[2], reverse=True)[i-1] if i in range(1, len(test_cases[2])+1) else -1)
        for i in range(len(test_cases[3])+2):
            self.assertEqual(test3.calculate_kth_highest_price(i), sorted(test_cases[3], reverse=True)[i-1] if i in range(1, len(test_cases[3])+1) else -1)
        for i in range(len(test_cases[4])+2):
            self.assertEqual(test4.calculate_kth_highest_price(i), sorted(test_cases[4], reverse=True)[i-1] if i in range(1, len(test_cases[4])+1) else -1)
        for i in range(len(test_cases[5])+2):
            self.assertEqual(test5.calculate_kth_highest_price(i), sorted(test_cases[5], reverse=True)[i-1] if i in range(1, len(test_cases[5])+1) else -1)
        for i in range(len(test_cases[6])+2):
            self.assertEqual(test6.calculate_kth_highest_price(i), sorted(test_cases[6], reverse=True)[i-1] if i in range(1, len(test_cases[6])+1) else -1)
        for i in range(len(test_cases[7])+2):
            self.assertEqual(test7.calculate_kth_highest_price(i), sorted(test_cases[7], reverse=True)[i-1] if i in range(1, len(test_cases[7])+1) else -1)
        for i in range(len(test_cases[8])+2):
            self.assertEqual(test8.calculate_kth_highest_price(i), sorted(test_cases[8], reverse=True)[i-1] if i in range(1, len(test_cases[8])+1) else -1)
        for i in range(len(test_cases[9])+2):
            self.assertEqual(test9.calculate_kth_highest_price(i), -1)
        for i in range(len(test_cases[10])+2):
            self.assertEqual(test10.calculate_kth_highest_price(i), sorted(test_cases[10], reverse=True)[i-1] if i in range(1, len(test_cases[10])+1) else -1)
        for i in range(len(test_cases[11])+2):
            self.assertEqual(test11.calculate_kth_highest_price(i), sorted(test_cases[11], reverse=True)[i-1] if i in range(1, len(test_cases[11])+1) else -1)
        for i in range(len(test_cases[11])+2):
            self.assertEqual(test12.calculate_kth_highest_price(i), sorted(test_cases[12], reverse=True)[i-1] if i in range(1, len(test_cases[12])+1) else -1)

class Room_Reserve_API_Test(unittest.TestCase):
    def test_room_reserve(self):
        test1 = Room_Reserve_API()
        test2 = Room_Reserve_API()

        self.assertTrue(test1.reserve("ColumbiaSC-Room101"))
        self.assertTrue(test1.reserve("HiltonLasVegas-1308"))
        self.assertTrue(test1.reserve("WaldorfAstoria-PenthouseA"))
        self.assertFalse(test1.reserve(""))
        self.assertFalse(test1.reserve("ColumbiaSC-Room101"))
        self.assertFalse(test1.reserve("HiltonLasVegas-1308"))
        self.assertFalse(test1.reserve("WaldorfAstoria-PenthouseA"))
        self.assertTrue(test1.reserve("HiltonLasVegas-1309"))
        self.assertFalse(test1.reserve("HiltonLasVegas-1309"))
        self.assertTrue(test1.reserve("a"))
        self.assertFalse(test1.reserve("A"))
        self.assertTrue(test1.reserve("aa"))
        self.assertFalse(test1.reserve("A"))
        self.assertFalse(test1.reserve("CoLuMbIaSc-rOom101"))

        self.assertTrue(test2.reserve("ColumbiaSC-Room101"))
        self.assertTrue(test2.reserve("HiltonLasVegas-1308"))
        self.assertTrue(test2.reserve("WaldorfAstoria-PenthouseA"))
        self.assertFalse(test2.reserve(""))
        self.assertFalse(test2.reserve("ColumbiaSC-Room101"))
        self.assertFalse(test2.reserve("HiltonLasVegas-1308"))
        self.assertFalse(test2.reserve("WaldorfAstoria-PenthouseA"))
        self.assertTrue(test2.reserve("HiltonLasVegas-1309"))
        self.assertFalse(test2.reserve("HiltonLasVegas-1309"))
        self.assertTrue(test2.reserve("a"))
        self.assertFalse(test2.reserve("A"))
        self.assertTrue(test2.reserve("aa"))
        self.assertFalse(test2.reserve("A"))
        self.assertFalse(test2.reserve("CoLuMbIaSc-rOom101"))

if __name__ == '__main__':
    unittest.main()
