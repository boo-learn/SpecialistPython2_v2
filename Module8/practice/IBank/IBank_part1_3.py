class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    def add_history(self, msg):
        self.__history.append(msg)

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.getter
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        self.add_history(f"Пополнение {amount} руб.")

    def withdraw(self, amount: int, commission: int = 0) -> None:
        if amount + (amount * commission / 100) <= self.__balance:
            self.__balance -= amount + (amount * commission / 100)
            self.add_history(f"Снятие {amount} руб.")
        else:
            raise ValueError("Денег на счету недостаточно")

    def transfer(self, target_account: 'Account', amount: int, comission: int = 0) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :param comission: процент за перевод
        :return:
        """
        if self.__balance >= amount:
            self.__balance -= amount + amount * (comission / 100)
            target_account.__balance += self.__balance
            self.add_history(f"Перевод {amount} руб. на счёт клиента: {target_account.name}")
            target_account.add_history(f"Перевод {amount} руб. на счёт клиента: {self.name}")
        else:
            raise ValueError("Недостаточно денег на счёте")


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "3232 456124", "+7-901-744-22-99", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
try:
    account1.transfer(account2, 500, 2)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
# print(account1)
# print(account2)

# # Переводим еще с первого аккаунт на второй:
# try:
#     account1.transfer(account2, 600, 2)
# except ValueError as e:
#     print(e)

print(account1)
print(account2)


# Проверяем изменения баланса:
print(account1)
print(account2)
