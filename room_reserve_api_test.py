import unittest
from room_reserve_api import Room_Reserve_API


class Room_Reserve_API_Test(unittest.TestCase):
    def unit_test(self):
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
        self.assertTrue(test1.reserve("A"))
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
        self.assertTrue(test2.reserve("A"))
        self.assertTrue(test2.reserve("aa"))
        self.assertFalse(test2.reserve("A"))
        self.assertFalse(test2.reserve("CoLuMbIaSc-rOom101"))

if '__name__':
    unittest.main()
