import unittest
from CsvReader import CsvReader
from Calculator import Calculator
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_addition_calculator(self):
        test_data = CsvReader('/src/Addition.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_subtraction_calculator( self ):
        test_data = CsvReader('/src/Subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_method_calculator(self):
        test_data = CsvReader('/src/Multiplication.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row ['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CsvReader('/src/Division.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.division(row['Value 2'], row ['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))


    def test_square_method_calculator(self):
        test_data = CsvReader ('/src/Unit_square.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))

    def test_squareRoot_method_calculator(self):
        test_data = CsvReader ('/src/Unit_test_square_root.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.squareRoot(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

if __name__ == '__main__':
   unittest.main()
