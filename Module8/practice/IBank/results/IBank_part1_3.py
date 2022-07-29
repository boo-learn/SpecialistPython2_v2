class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance

    @property
    def balance(self):
        return self.__balance

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.__balance >= amount:
            target_account.__balance += amount
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств на балансе")

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств на балансе")

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    # TODO-1: добавьте проверку паспорта и телефона(в конструкторе) на соответствие заданным форматам
    #  В случае несоответствия выбрасываем исключение ValueError("Неверный формат телефона/паспорта")
    #  Проверка информации на корректность - валидация
    #  Готовые валидаторы можете взять в директории helpers


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно
try:
    account1.transfer(account2, 10)
except ValueError as e:
    print(e)
