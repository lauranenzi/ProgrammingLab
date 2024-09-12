import unittest

from esParte6 import CSVFile

# Testing
class TestCSVFile(unittest.TestCase):
    
    def test_init(self):
    
        csv_file = CSVFile('test_file.csv')
        self.assertEqual(csv_file.name, 'test_file.csv')


    def test_start_end(self):
        csv_file = CSVFile('test_file.csv')
        data = csv_file.get_data(start=1, end=2)
        self.assertEqual(data[0][0], '1949-02')
        