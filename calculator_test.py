import unittest

# This is the class we want to test. So, we need to import it
import Calculator as CalculatorClass

class Test(unittest.TestCase):
    calculator = CalculatorClass.Calculator() # instantiate the Calculator Class
    def test_0_add(self):
        result = self.calculator.add(4,8)
        self.assertEqual(result,12)

    def test_1_multiply(self):
        result2 = self.calculator.multiply(3,9)
        self.assertEqual(result2,27)

    def test_2_power(self):
        result3 = self.calculator.power(2,3)
        self.assertEqual(result3,8)


       
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()