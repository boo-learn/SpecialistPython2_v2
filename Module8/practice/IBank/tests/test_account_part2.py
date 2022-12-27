from typing import List
import pytest
from IBank_part2 import Account, Operation


@pytest.fixture
def account() -> Account:
    return Account(name="Иван", passport="3230 634563", phone_number="+7-900-765-12-34", start_balance=1000)


@pytest.fixture
def accounts() -> List[Account]:
    return [
        Account("Иван", "3002 123477", "+7-900-600-10-22", start_balance=200),
        Account("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300)
    ]


##########################
# Тесты истории операций #
##########################

def test_operation_deposit(account: Account):
    assert len(account.get_history()) == 0  # На новом аккаунте не должно быть операций
    account.deposit(500)
    account.deposit(200)
    assert len(account.get_history()) == 2  # Должны быть добавлены ровно две операции
    assert Operation.DEPOSIT in str(account.get_history()[0])
    assert "500" in str(account.get_history()[0])
    assert Operation.DEPOSIT in str(account.get_history()[1])
    assert "200" in str(account.get_history()[1])


def test_operation_withdraw(account: Account):
    assert len(account.get_history()) == 0
    account.withdraw(100)
    assert len(account.get_history()) == 1
    assert Operation.WITHDRAW in str(account.get_history()[0])
    assert "100" in str(account.get_history()[0])


def test_operation_withdraw_raise(account: Account):
    assert len(account.get_history()) == 0
    with pytest.raises(ValueError):
        account.withdraw(1200)
    assert len(account.get_history()) == 0


def test_operation_transfer(accounts: List[Account]):
    sum_transfer = 200  # Сумма перевода
    account_sender, account_recipient = accounts
    account_sender.transfer(account_recipient, sum_transfer)

    assert len(account_sender.get_history()) == 1
    assert len(account_recipient.get_history()) == 1

    assert Operation.TRANSFER_OUT in str(account_sender.get_history()[0])
    assert Operation.TRANSFER_IN in str(account_recipient.get_history()[0])

    assert str(sum_transfer) in str(account_sender.get_history()[0])
    assert str(sum_transfer) in str(account_recipient.get_history()[0])

    assert account_recipient.name in str(account_sender.get_history()[0])
    assert account_sender.name in str(account_recipient.get_history()[0])


def test_operation_transfer_raise(accounts: List[Account]):
    sum_transfer = 250  # Сумма перевода
    account_sender, account_recipient = accounts

    with pytest.raises(ValueError):
        account_sender.transfer(account_recipient, sum_transfer)

    assert len(account_sender.get_history()) == 0
    assert len(account_recipient.get_history()) == 0
