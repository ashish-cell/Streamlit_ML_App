import unittest
import tempfile
import os
import pandas as pd 

from data_loader import read_csv, read_excel, read_url



class TestCSVLoading(unittest.TestCase):

    def test_read_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # create a temporary CSV file
            csv_file = os.path.join(tmpdir, 'test.csv')
            with open(csv_file, 'w') as f:
                f.write('a,b,c\n1,2,3\n4,5,6\n')
            # read data from the temporary CSV file
            df = read_csv(csv_file)
            # check if the data has been read correctly
            self.assertEqual(df.shape, (2, 3))
            self.assertEqual(list(df.columns), ['a', 'b', 'c'])
            self.assertEqual(list(df['a']), [1, 4])

class TestExcelLoading(unittest.TestCase):

    def test_read_excel(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # create a temporary Excel file
            excel_file = os.path.join(tmpdir, 'test.xlsx')
            df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
            df.to_excel(excel_file, sheet_name='Sheet1', index=False)
            # read data from the temporary Excel file
            df = read_excel(excel_file, sheet_name='Sheet1')
            # check if the data has been read correctly
            self.assertEqual(df.shape, (2, 2))
            self.assertEqual(list(df.columns), ['a', 'b'])
            self.assertEqual(list(df['b']), [3, 4])

class TestURLLoading(unittest.TestCase):

    def test_read_url(self):
        # read data from a URL
        df = read_url('https://archive.ics.uci.edu/ml/machine-learning-databases/blood-transfusion/transfusion.data')
        # check if the data has been read correctly
        self.assertEqual(df.shape, (748, 5))
        self.assertEqual(list(df.columns), ['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)',
       'Time (months)', 'whether he/she donated blood in March 2007'])


if __name__ == '__main__':
    unittest.main()



