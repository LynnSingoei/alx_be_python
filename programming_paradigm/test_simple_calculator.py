import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(-2,3),-5)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,3),15)
        self.assertEqual(self.calc.multiply(-2,3),-6)
        self.assertEqual(self.calc.multiply(-2,-3),6)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,5),2)
        self.assertEqual(self.calc.divide(-2,0),"None")
    

    