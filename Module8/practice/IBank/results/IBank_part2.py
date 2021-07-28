class Operation:
    # класс для хранение информации об операциях
    def __init__(self, ):
        # Тут добавляем свойства для хранение информации об операции
        operations = []



    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        if Account.deposit(self.amount):
            return f"Пополнение +{amount}"
        if Account.withdraw(self.amount):
            return f"Списание +{amount}"



class Account:
    pass
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор

    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposit(amount)

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise Exception("Not enought money")
        self.balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"Имя {self.name} \n passport {self.passport} \n phone {self.phone_number} \n balance {self.balance}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f" {self.name} баланс: {self.balance}"


    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
         """
        pass


ac1 = Account(name='Konstantin',
              passport='123456789',
              phone_number='89011234567',
              start_balance=0)

ac2 = Account(name='Ivan',
              passport='987654321',
              phone_number='89076543210',
              start_balance=0)

print(ac1.full_info())
print(ac2.full_info())

ac1.deposit(500)

print(ac1)
print(ac2)

ac1.transfer(ac2, 100)
