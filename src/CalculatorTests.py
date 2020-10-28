import unittest
from CsvReader import CsvReader
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator( self ):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_addition_calculator( self ):
        test_data = CsvReader('/src/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_multiplication_method_calculator( self ):
        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
