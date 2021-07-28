import unittest
from ... import Account


# FIXME: Допишите тест/тесты, который выявит недоработки в классе Account ,
#  затем исправьте недоработки класса, чтобы тест проходил
class TestAccountTask2(unittest.TestCase):
    def setUp(self):
        self.accounts = [Account("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300),
                         Account("Иван", "3002 123477", "+7-900-600-10-22", start_balance=100),
                         ]

    def test_deposit(self):
        self.accounts[0].deposit(500)
        self.assertEqual(self.accounts[0].balance, 800)

    def test_withdraw(self):
        self.accounts[0].withdraw(200)
        self.assertEqual(self.accounts[0].balance, 96)  # С учетом комиссии в 2%

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.accounts[0].withdraw(600)

    def test_transfer(self):
        self.accounts[0].transfer(self.accounts[1], 200)  # С учетом комиссии в 2%
        self.assertEqual(self.accounts[0].balance, 96)
        self.assertEqual(self.accounts[1].balance, 300)

    def test_transfer_raise(self):
        with self.assertRaises(ValueError):
            self.accounts[0].transfer(self.accounts[1], 500)

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.accounts[0].full_info())
        self.assertIn("3002 123456", self.accounts[0].full_info())
        self.assertIn("+7-900-600-10-20", self.accounts[0].full_info())
        self.assertIn("Петр", self.accounts[0].full_info())

    def test_validate_passport(self):
        pass

    def test_validate_phone(self):
        pass