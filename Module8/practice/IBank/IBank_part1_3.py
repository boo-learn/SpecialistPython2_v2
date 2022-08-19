import re

class Account:
    # TODO-0: скопируйте реализацию из предыдущего решения
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = self.check_passport(passport)
        self.phone_number = self.check_phone_number(phone_number)
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу

    def check_passport(self, passport):
        passport_rule = re.compile(r'\d{4}\s\d{6}') # yyyy xxxxxx
        if passport_rule.search(passport):
            self.passport = passport
            return self.passport
        else:
            raise ValueError(f'{passport} - неверно введён паспорт, требуется "yyyy xxxxxx"')

    def check_phone_number(self, number):
        number_rule = re.compile(r'[+7-9]\d{2}-\d{3}-\d{2}-\d{2}') #+7-9xx-xxx-xx-xx
        if number_rule.search(number):
            self.phone_number = number
            return self.phone_number
        else:
            raise ValueError(f'{number} - неверно введён номер телефона, требуется "+7-9xx-xxx-xx-xx"')

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount > self.balance:
            raise ValueError("У Вас недостаточно средств")

        self.balance -= amount

    # TODO-1: напишите реализацию метода transfer()
    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
try:
    account1.transfer(account2, 500)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)

# Переводим еще с первого аккаунт на второй:
try:
    account1.transfer(account2, 600)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)
