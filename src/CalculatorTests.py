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

if __name__ == '__main__':
    unittest.main()
