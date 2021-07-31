import unittest
from ..results.IBank_part4 import CreditAccount, Operation


class TestCreditAccountHistory(unittest.TestCase):
    def setUp(self):
        self.account1 = CreditAccount("Иван", "3002 123477", "+7-900-600-10-77",
                                      start_balance=300, negative_limit=500)
        self.account2 = CreditAccount("Василий", "3002 123445", "+7-900-600-10-45",
                                      start_balance=100, negative_limit=200)

    def test_deposit_history(self):
        self.account1.deposit(500)
        self.assertIn(Operation.DEPOSIT, self.account1.show_history())
        self.assertIn("500", self.account1.show_history())

    def test_withdraw_history_with_fee(self):
        self.account1.withdraw(500)
        self.assertIn(Operation.WITHDRAW, self.account1.show_history())
        self.assertIn("500", self.account1.show_history())
        self.assertIn("10", self.account1.show_history())

    def test_withdraw_transfer_with_fee(self):
        self.account1.transfer(self.account2, 200)
        self.assertIn(Operation.TRANSFER, self.account1.show_history())
        self.assertIn("200", self.account1.show_history())  # сумма перевода
        self.assertIn("Василий", self.account1.show_history())
        self.assertIn("4", self.account1.show_history())  # комиссия перевода

        self.assertIn(Operation.INCOME, self.account2.show_history())
        self.assertIn("200", self.account2.show_history())
        self.assertIn("Иван", self.account2.show_history())

    def test_chain_operation_history(self):
        pass
        #  TODO: допишите тесты истории нескольких операций (3-4 операции в данном тесте)
