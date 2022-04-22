# Сюда отправляем готовое решение IBank часть-2

class Operation:
    # класс для хранение информации об операциях
    def __init__(self, type, amount, where = None, target_account = None):
        self.type = type
        self.amount = amount
        self.where = where
        self.target_account = target_account
    def __repr__(self):
        if self.where == None and self.target_account == None:
            return f"{self.type} {self.amount}"
        else:
            return f"{self.type} {self.amount} {self.where} {self.target_account}"


class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

    def full_info(self):
        return f"{self.name} баланс: {self.__balance}. Паспорт: {self.passport} т. {self.phone_number}"

    @property
    def balance(self):
        return self.__balance


    def __repr__(self):
        return f"{self.name} баланс: {self.__balance}."


    def deposit(self, amount):
        self.__balance += amount
        new_operatoin = Operation('Пополнение', amount)
        self.__history.append(new_operatoin)


    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        new_operation = Operation('Снятие', amount)
        self.__history.append(new_operation)


    def transfer(self, target_account, amount):
        self.withdraw(amount)
        new_operation = Operation('Перевод',amount,'на счет клиента:', target_account.name )
        self.__history.append(new_operation)
        target_account.deposit(amount)
        new_operation = Operation('Поступление', amount, where='со счета клиента:', target_account=self.name)
        self.__history.append(new_operation)


    def show_history(self):
        hist_operations = ""
        for operation in self.__history:
            hist_operations += str(operation) + "\n"
        return hist_operations

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "3540 193565", "+7-900-765-12-86", 200)
account1.deposit(500)
account1.deposit(1000)
account1.transfer(account2, 600)
account1.withdraw(100)

print(account1.show_history())
