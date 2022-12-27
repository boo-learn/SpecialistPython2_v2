# Как запустить тесты?
# Смотри в 'tasks/run_test.md'

from typing import List
import pytest
from IBank_part1_3 import Account


@pytest.fixture
def account() -> Account:
    return Account(name="Иван", passport="3230 634563", phone_number="+7-900-765-12-34", start_balance=1000)


@pytest.fixture
def accounts() -> List[Account]:
    return [
        Account("Иван", "3002 123477", "+7-900-600-10-22", start_balance=200),
        Account("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300)
    ]


def test_create_account(account: Account):
    assert account.name == "Иван"
    assert account.passport == "3230 634563"
    assert account.phone_number == "+7-900-765-12-34"
    assert account.balance == 1000


def test_full_info(account: Account):
    # format: "Иван баланс: 100 руб. паспорт: 3230 634563 т.+7-900-765-12-34"
    assert "Иван" in account.full_info()
    assert "1000 руб" in account.full_info()
    assert "3230 634563" in account.full_info()
    assert "+7-900-765-12-34" in account.full_info()


def test_deposit(account: Account):
    assert account.balance == 1000
    account.deposit(400)
    assert account.balance == 1400
    account.deposit(200)
    assert account.balance == 1600


def test_withdraw(account: Account):
    assert account.balance == 1000
    account.withdraw(500)
    assert account.balance == 500


def test_withdraw_raise(account: Account):
    with pytest.raises(ValueError):
        account.withdraw(1200)
    assert account.balance == 1000


def test_transfer(accounts: List[Account]):
    account1, account2 = accounts
    assert account1.balance == 200
    assert account2.balance == 300
    account1.transfer(account2, 100)
    assert account1.balance == 100
    assert account2.balance == 400


def test_transfer_raise(accounts: List[Account]):
    account1, account2 = accounts
    assert account1.balance == 200
    assert account2.balance == 300
    with pytest.raises(ValueError):
        account1.transfer(account2, 250)
    assert account1.balance == 200
    assert account2.balance == 300
