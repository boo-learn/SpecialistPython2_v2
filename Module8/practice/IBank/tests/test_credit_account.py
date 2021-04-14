import unittest
from ... import CreditAccount

class TestCreditAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = CreditAccount("Иван", 12345678, "+7900-600-10-20",
                                     start_balance=300, negative_limit=-500)
        self.account2 = CreditAccount("Василий", 12345676, "+7900-600-10-22",
                                      start_balance=100, negative_limit=-200)

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
        self.account1.withdraw(400) # уходим в -баланс. Тут 2%
        self.account1.withdraw(200) # снимает при -балансе. Тут 5%
        self.assertEqual(self.account1.balance, -318)

    def test_withdraw_raise(self):
        with self.assertRaises(ValueError):
            self.account1.withdraw(900)

    def test_transfer(self):
        self.account1.transfer(self.account2, 200)
        self.assertEqual(self.account1.balance, 96)
        self.assertEqual(self.account2.balance, 300)

    def test_to_archive(self):
        self.account1.to_archive()
        self.assertTrue(self.account1.in_archive)

    def test_restore_from_archive(self):
        self.account1.to_archive()
        self.account1.restore()
        self.assertEqual(self.account1.balance, 0)
        self.assertFalse(self.account1.in_archive)

    def test_to_archive_negative_balance(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, -210)
        with self.assertRaises(ValueError) as error:
            self.account1.to_archive()
        # Можно так, если нужно проверить определенный текст ошибки, но как правило так не делают
        # self.assertTrue('Нельзя убрать счет с отрицательным балансом в архив' in str(error.exception))

    def test_full_info(self):
        # Проверяем наличие информации в строке, а не строгий формат
        self.assertIn("300", self.account1.full_info())
        self.assertIn("Иван", self.account1.full_info())
        self.assertIn("+7900-600-10-20", self.account1.full_info())
        self.assertIn("<K>", self.account1.full_info())