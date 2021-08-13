import unittest
from stock_profit import Stock


class MyTestCase(unittest.TestCase):
    def test_stock_profit(self):
        test_cases = [ [1,2,3,4,5,6,7,8,9,10],
                       [10,9,8,7,6,5,4,3,2,1],
                       [3,3,99,100,3985,83,9,0,39,10,5],
                       [3,2,4,5,20,0,1000,10001,4,5,399],
                       [1,2,3,5,99999,999999],
                       [4,50034,1,400000,3,2,4,999]]


        test_answers = [9, 0, 3982, 10001, 999998, 399999]

        test0 = Stock(test_cases[0])
        test1 = Stock(test_cases[1])
        test2 = Stock(test_cases[2])
        test3 = Stock(test_cases[3])
        test4 = Stock(test_cases[4])
        test5 = Stock(test_cases[5])

        self.assertEqual(test0.calculate_max_profit(), test_answers[0])
        self.assertEqual(test1.calculate_max_profit(), test_answers[1])
        self.assertEqual(test2.calculate_max_profit(), test_answers[2])
        self.assertEqual(test3.calculate_max_profit(), test_answers[3])
        self.assertEqual(test4.calculate_max_profit(), test_answers[4])
        self.assertEqual(test5.calculate_max_profit(), test_answers[5])

        self.assertEqual(test0.calculate_kth_highest_price(2)[-1], sorted(test_cases[0], reverse=True)[1])
        self.assertEqual(test1.calculate_kth_highest_price(2)[-1], sorted(test_cases[1], reverse=True)[1])
        self.assertEqual(test2.calculate_kth_highest_price(2)[-1], sorted(test_cases[2], reverse=True)[1])
        self.assertEqual(test3.calculate_kth_highest_price(2)[-1], sorted(test_cases[3], reverse=True)[1])
        self.assertEqual(test4.calculate_kth_highest_price(2)[-1], sorted(test_cases[4], reverse=True)[1])
        self.assertEqual(test5.calculate_kth_highest_price(2)[-1], sorted(test_cases[5], reverse=True)[1])



        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
