"""
Дескриптор, автоматически вычитает комиссию с значения amount объекта Account
"""


class Value:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value - value * instance.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
