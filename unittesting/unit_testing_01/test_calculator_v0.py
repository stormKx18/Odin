import unittest
import calculator

#python3 -m unittest test_calculator_v0.py
#python3 -m unittest test_calculator_v0.py -v

class TestsCalculator(unittest.TestCase):
    def test_add_functionality(self):
        result = calculator.calc_add(10,20)
        self.assertEqual(result,30)

    def test_add_functionality_two_negative_numbers(self):
        result = calculator.calc_add(-10,-20)
        self.assertEqual(result,-30)

    
