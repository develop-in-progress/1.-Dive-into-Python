import descriptor
import unittest

"""Класс Account создает объект, с значения amount которого снимается указанная комиссия при присвоении amount. 
Проверяем правильность снятия комиссии"""


class TestDescriptor(unittest.TestCase):
    def setUp(self):
        self.comission = 0.1
        self.new_account = descriptor.Account(0.1)
        self.new_account.amount = 100
        self.amount = 100

    def test_right_comission(self):
        self.assertEqual(self.new_account.amount, self.amount-self.amount*self.comission)


if __name__ == '__main__':
    unittest.main()
