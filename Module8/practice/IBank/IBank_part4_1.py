# Сюда отправляем готовое решение IBank часть-4
class Operation:
    # TODO-0: сюда копируем реализацию класса Operation из предыдущей задачи
    pass


class Account:
    pass
    # TODO-0: сюда копируем реализацию класса Account из предыдущей задачи


# TODO-1: Создаем класс для кредитного аккаунта, наследуясь от аккаунта
class CreditAccount(Account):
    Credit_Commission = 0.05

    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.negative_limit = negative_limit
        self.__history = []

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.balance} руб."

    @staticmethod
    def amount_with_credit_commission(amount):
        return amount + int(amount * CreditAccount.Credit_Commission)

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int, to_history: bool = True) -> None:
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        if self.__balance < 0 and (self.__balance - self.amount_with_credit_commission(amount)) < -self.negative_limit:
            print(ValueError("Превышен кредитный лимит"))
        if self.__balance < 0 and (self.__balance - self.amount_with_credit_commission(amount)) >= -self.negative_limit:
            self.__balance -= self.amount_with_credit_commission(amount)
        if self.__balance >= 0:
            self.__balance -= self.amount_with_commission(amount)
