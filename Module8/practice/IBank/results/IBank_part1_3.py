


class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance  # Закрываем прямой доступ к балансу

    # TODO: совместно с преподавателем реализуйте getter для просмотра баланса
    #  Можете попробовать самостоятельно: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/
    @property
    def balance(self):
        return self.__balance

    def zero_check(self,amount):
        if amount <= 0:
            raise ValueError(f'Нельзя ввести сумму меньше нуля')

    def limit_check(self,amount):
        if amount > self.balance:
            raise ValueError(f'Сумма первышает доступный лимит')

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if not self.zero_check(amount) and not self.limit_check(amount):
            target_account.__balance += amount
            self.__balance -= amount

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if not self.zero_check(amount):
            self.__balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if not self.zero_check(amount) and not self.limit_check(amount):
                self.__balance -= amount


    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name}, баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name}, баланс: {self.__balance} руб."


# Создаем тестовый аккаунт:
account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", start_balance=500)
account2 = Account("Иван", passport="3230 634563", phone_number="+7-900-765-12-34")
# Смотрим баланс:
print(account1)

# Вносим сумму на счет:
try:
    account1.deposit(-600)
except ValueError as e:
    print(e)
print(account1)


print("снимаем:")
# Снимаем деньги со счета:
try:
    account1.withdraw(10000)
except ValueError as e:
    print(e)
print(account1)

# Пробуем снять еще:
try:
    account1.withdraw(-1000)
except ValueError as e:
    print(e)
print(account1)
print(account1.balance)

try:
    account1.transfer(account2,1000)
except ValueError as e:
    print(e)
print(account1)
print(account1.balance)
print(account2)
print(account1.balance)

try:
    account1.transfer(account2,10)
except ValueError as e:
    print(e)
print(account1)
print(account1.balance)
print(account2)
print(account1.balance)
