import unittest
from fileReader import FileReader
import tempfile
import os


class TestFileReader(unittest.TestCase):
    def setUp(self):
        path_to_test_file = os.path.join(tempfile.gettempdir(), 'test.data')
        path_to_wrong_test_file = os.path.join(tempfile.gettempdir(), 'no_file')
        with open(path_to_test_file, 'w') as f:
            f.write('test info')
        self.wrong_reader = FileReader(path_to_wrong_test_file)
        self.reader = FileReader(path_to_test_file)
        self.text = self.reader.read()

    def test_correct_reading(self):
        self.assertEqual(self.text, 'test info')

    def test_wrong_file(self):
        self.assertFalse(self.wrong_reader.read())


if __name__ == '__main__':
    unittest.main()
