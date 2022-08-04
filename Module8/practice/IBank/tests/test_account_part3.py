from typing import List
import pytest
from IBank_part3 import Account


@pytest.fixture
def account() -> Account:
    return Account(name="Иван", passport="3230 634563", phone_number="+7-900-765-12-34", start_balance=1000)


@pytest.fixture
def accounts() -> List[Account]:
    return [
        Account("Иван", "3002 123477", "+7-900-600-10-22", start_balance=200),
        Account("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300)
    ]


###########################
# Тесты с учетом комиссии #
###########################

# Тестируем только те методы, которые приводят к снятию комиссии

def test_withdraw(account: Account):
    assert account.balance == 1000
    account.withdraw(200)
    assert account.balance == 796  # С учетом комиссии 2%
    account.withdraw(540)
    assert account.balance == 246  # Комиссию округляем вниз


def test_withdraw_raise(account: Account):
    assert account.balance == 1000
    with pytest.raises(ValueError):
        account.withdraw(1000)  # Всю сумму снять нельзя, нужно учесть комиссию
    assert account.balance == 1000


def test_transfer(accounts: List[Account]):
    account1, account2 = accounts
    assert account1.balance == 200
    assert account2.balance == 300
    account1.transfer(account2, 100)
    assert account1.balance == 98  # Комиссия берется только с отправителя
    assert account2.balance == 400


def test_transfer_raise(accounts: List[Account]):
    account1, account2 = accounts
    assert account1.balance == 200
    assert account2.balance == 300
    with pytest.raises(ValueError):
        account1.transfer(account2, 200) # Всю сумму перевести нельзя, нужно учесть комиссию
    assert account1.balance == 200
    assert account2.balance == 300
