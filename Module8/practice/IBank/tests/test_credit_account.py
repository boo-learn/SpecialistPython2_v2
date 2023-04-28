from typing import List
import pytest
from Module8.practice.IBank.IBank_part4_2 import CreditAccount


@pytest.fixture
def credit_account() -> CreditAccount:
    return CreditAccount(name="Иван", passport="3230 634563", phone_number="+7-900-765-12-34",
                         start_balance=500, negative_limit=200)


@pytest.fixture
def credit_accounts() -> List[CreditAccount]:
    return [
        CreditAccount("Иван", "3002 123477", "+7-900-600-10-22", start_balance=200, negative_limit=100),
        CreditAccount("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300, negative_limit=150)
    ]


#############################
# Тесты кредитного аккаунта #
#############################

def test_full_info(credit_account: CreditAccount):
    # format: "<К> Иван баланс: 500 руб. паспорт: 3230 634563 т.+7-900-765-12-34"
    assert "<К>" in credit_account.full_info()
    assert "Иван" in credit_account.full_info()
    assert "500 руб" in credit_account.full_info()
    assert "3230 634563" in credit_account.full_info()
    assert "+7-900-765-12-34" in credit_account.full_info()


def test_deposit(credit_account: CreditAccount):
    assert credit_account.balance == 500
    credit_account.deposite(400)
    assert credit_account.balance == 900


def test_withdraw(credit_account: CreditAccount):
    assert credit_account.balance == 500
    credit_account.withdraw(200)
    assert credit_account.balance == 796  # С учетом комиссии 2%
    credit_account.withdraw(540)
    assert credit_account.balance == 246  # Комиссию округляем вниз


def test_withdraw_limit(self):
    assert credit_account.balance == 500
    self.account1.withdraw(600)
    self.assertEqual(self.account1.balance, -112)  # С учетом комиссии в 2%


def test_withdraw_limit_max(self):
    assert credit_account.balance == 500
    with self.assertRaises(ValueError):
        self.account1.withdraw(700)  # При балансе 500 и кредите 200, нельзя снять 700, т.к. есть комиссия


def test_withdraw_inc_commission_on_negative_balance(self):
    assert credit_account.balance == 500
    self.account1.withdraw(600)
    self.assertEqual(self.account1.balance, -112)  # уходим в -баланс. Комиссия 2%, т.к. до снятия был положительный баланс
    self.account1.withdraw(50)  # снимаем при -балансе. Комиссия 5% (2 рубля с 50)
    self.assertEqual(self.account1.balance, -164)


def test_transfer(accounts: List[CreditAccount]):
    """
    Проверяем успешный перевод средств между кредитными счетами(аккаунтами)
    """
    # TODO: напишите данный тест самостоятельно
    pass


def test_transfer_raise(accounts: List[CreditAccount]):
    """
    Проверяем перевод, при нехватке суммы на счету отправителя даже с учетом кредита, между кредитными счетами(аккаунтами)
    """
    # TODO: напишите данный тест самостоятельно
    pass
