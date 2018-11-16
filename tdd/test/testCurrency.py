import unittest
from currency import BritishPound, Dollar


class MyTest(unittest.TestCase):

    def testMultiplication(self):
        five = BritishPound(5)
        result: BritishPound = five.times(2)
        self.assertEqual(10, result.amount)

        result: BritishPound = five.times(3)
        self.assertEqual(15, result.amount)

    def testEqual(self):
        self.assertTrue(BritishPound(5) == BritishPound(5))
        self.assertFalse(BritishPound(5) == BritishPound(6))

    def testDollarMultiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))