# Сюда отправляем готовое решение IBank часть-2

class Operation:
    # класс для хранение информации об операциях
    # Пополнение, Снятие, Перевод, Поступление
    def __init__(self, type, amount, target_account=None):
        # Тут добавляем свойства для хранение информации об операции
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        if self.type in ("Пополнение", "Снятие"):
            return f"{self.type} {self.amount} руб."
        elif self.type == "Перевод":
            return f"{self.type} {self.amount} руб. на счет клиента: {self.target_account.name}"
        else:
            return f"{self.type} {self.amount} руб. со счета клиента: {self.target_account.name}"


class Account:
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор:
    #   self.__history = []
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)
        self.__history.pop()
        target_account.__history.pop()
        op_transfer_to = Operation("Перевод", amount, target_account)
        op_transfer_in = Operation("Поступление", amount, self)
        self.__history.append(op_transfer_to)
        target_account.__history.append(op_transfer_in)

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        new_op = Operation("Пополнение", amount)
        self.__history.append(new_op)

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < amount:
            raise ValueError("Денег на счету недостаточно!")

        self.__balance -= amount
        new_op = Operation("Снятие", amount)
        self.__history.append(new_op)

    @property
    def balance(self):
        return self.__balance

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        operations = ""
        for op in self.__history:
            operations += str(op) + '\n'
        return operations


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", start_balance=300)
account2 = Account("Алексей", "3232 456124", "+7-901-744-22-99", start_balance=500)

account1.deposit(100)
account1.deposit(200)
account1.withdraw(200)

account1.transfer(account2, 150)

print(account1.show_history())
print("-----")
print(account2.show_history())

