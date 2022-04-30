import unittest
from ..results.IBank_part4 import CreditAccount


# FIXME: Обратите внимание! Если какой-то тест никак не проходит, проверьте корректность самого теста
#   P.S. Тут присутствует тест, в котором специально допущена ошибка!
class TestCreditAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = CreditAccount("Иван", "3002 123477", "+7-900-600-10-77",
                                      start_balance=300, negative_limit=500)
        self.account2 = CreditAccount("Василий", "3002 123445", "+7-900-600-10-45",
                                      start_balance=100, negative_limit=200)

    def test_deposit(self):
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 800)

    def test_withdraw(self):
        self.account1.withdraw(200)
        self.assertEqual(self.account1.balance, 96)  # С учетом комиссии в 2%

    def test_withdraw_limit(self):
        self.account1.withdraw(400)
        self.assertEqual(self.account1.balance, -108)  # С учетом комиссии в 2%

    def test_withdraw_limit_max(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(800)

    def test_withdraw_inc_commission_on_negative_balance(self):
        self.account1.withdraw(400)  # уходим в -баланс. Комиссия 2%, т.к. до снятия был положительный баланс
        self.assertEqual(self.account1.balance, -108)
        self.account1.withdraw(200)  # снимает при -балансе. Комиссия 5%
        self.assertEqual(self.account1.balance, -318)

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(800)

    def test_transfer(self):
        self.account1.transfer(self.account2, 200)
        self.assertEqual(self.account1.balance, 96)
        self.assertEqual(self.account2.balance, 300)

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.account1.full_info())
        self.assertIn("Иван", self.account1.full_info())
        self.assertIn("+7-900-600-10-75", self.account1.full_info())
        self.assertIn("<К>", self.account1.full_info())
