import unittest
import json
from to_json import to_json

''' Тест проверяет работу декоратора @to_json, который преобразовывает данные функции в json формат'''


class JsonDataConvertTest(unittest.TestCase):
    def setUp(self):
        self.test_dict = {
            'Key': None,
            'Val': ['list', 5],
            'Set': (1, 2, 3)
        }

    @staticmethod
    @to_json
    def func_for_test(dict):
        return dict

    def test_right_conversion(self):
        self.assertEqual(JsonDataConvertTest.func_for_test(self.test_dict), json.dumps(self.test_dict))


if __name__ == '__main__':
    unittest.main()
