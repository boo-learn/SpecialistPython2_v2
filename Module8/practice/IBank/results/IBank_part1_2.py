class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance  # Закрываем прямой доступ к балансу

    # TODO: совместно с преподавателем реализуйте getter для просмотра баланса
    #  Можете попробовать самостоятельно: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        pass

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"..."

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"..."


# Создаем тестовый аккаунт:
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
