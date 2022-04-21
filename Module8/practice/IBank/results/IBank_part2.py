class Operation:
    # класс для хранение информации об операциях
    def __init__(self, type, amount, target_account=None): #replenishment, withdrawal, translation, admission):
        # Тут добавляем свойства для хранение информации об операции
        self.type = type
        self.amount = amount
        self.target_account = target_account


    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        return f'{self.type} {self.amount} {self.target_account}'

class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

    # def get_balance(self):
    #     return self.__balance

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
        # if self.__balance < amount:
        #     raise ValueError("Недостаточно денег")
        # elif self.__balance > amount:
        #     self.__balance -= amount
        #     target_account.__balance += amount
        self.withdraw(amount)
        target_account.deposit(amount)

        new_op = Operation(f'Перевод от пользователя: {account1.name}', f'средств в размере {amount} рублей', f'пользователю: {account2.name}')
        self.__history.append(new_op)

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        new_op = Operation('Пополнение средств в размере', f'{amount} рублей', f'на счет пользователя: {self.name}')
        self.__history.append(new_op)

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < amount:
            raise ValueError('Недостаточно средств')
        else:
            self.__balance -= amount
            new_op = Operation('Списание средств в размере', f'{amount} рублей', f'со счета пользователя: {self.name}')
            self.__history.append(new_op)

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

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        s = ''
        for operation in self.__history:
            s += str(operation) + '\n'
        return s

# try:
#     account1.withdraw()
# except ValueError as e:
#     print(e)

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)
account1.deposit(500)
print(account1.balance)
account1.withdraw(600)
print(account1.balance)
account1.transfer(account2, 300)
print(f'{account1}' + ', ' + f'{account2}')
# account2.withdraw(600)
print(account1.show_history())
