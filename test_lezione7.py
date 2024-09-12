import unittest

from Lez7 import somma
from esParte6 import CSVFile

# Testing
class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(1,1), 2)
        self.assertEqual(somma(1.5, 2.5), 4)

class TestCSVFile(unittest.TestCase):
    
    def test_init(self):
    
        csv_file = CSVFile('shampoo_sales.csv')

        self.assertEqual(csv_file.name, 'shampoo_sales.csv')