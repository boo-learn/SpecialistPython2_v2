class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        #self.balance = start_balance
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу

    def full_info(self) -> str:
        return f"{self.name} баланc: {self.balance}руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланc: {self.balance}руб."

    # TODO: реализуйте getter для просмотра баланса
    #  Подробнее тут: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/
    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError('Недостаточно денег на счёте.')



# Создаем тестовый аккаунт:
account1 = Account("Алексей", "3232 456124", "+7-901-744-22-99", start_balance=500)
print(account1.balance)

# Вносим сумму на счет:
account1.deposit(600)
print(account1)

# Снимаем деньги со счета:
try:
    account1.withdraw(1200)
    print(account1)
except ValueError as e:
    print(e)
print(account1)

# Пробуем снять еще:
try:
    account1.withdraw(1000)
    print(account1)
except ValueError as e:
    print(e)
    print(account1)
