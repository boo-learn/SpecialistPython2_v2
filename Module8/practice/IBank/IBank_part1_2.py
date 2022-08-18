class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance

    def full_info(self) -> str:

        return f"{self.name} баланс: {self.__balance}. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:

        return f"{self.name} баланс: {self.__balance}"

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if self.__balance < amount:
            print('недостаточно средств')
        else:
            self.__balance -= amount


account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", start_balance=500)

# Смотрим баланс:
print(account1)

# Вносим сумму на счет:
account1.deposit(600)
print(account1)

# Снимаем деньги со счета:
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
print(account1)

# Пробуем снять еще:
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
print(account1)
