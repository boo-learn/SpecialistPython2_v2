# Сюда отправляем готовое решение IBank часть-3
class Operation:
    # класс для хранение информации об операциях
    def __init__(self, amount, fee=0, source=None):
        # Тут добавляем свойства для хранение информации об операции
        #self.type=type
        self.amount=amount
        self.source=source
        self.fee = fee

    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        if self.source is None:
            if self.amount>0:
                text=(f"Пополнение +{self.amount} руб.")
            else:
                text=(f"Списание {self.amount} руб. (комиссия: -{self.fee} руб)")
        else:
            if self.amount>0:
                text=(f"Поступление +{self.amount} руб. со счета клиента {self.source}")
            else:
                text=(f"Перевод {self.amount} руб. на счет клиента {self.source} (комиссия: -{self.fee} руб)")
        return text

class Account:
    FEE=0.02
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance
        self.history = []
        self.in_archive=False

    def transfer(self, target_account, amount):
        if self.in_archive or target_account.in_archive:
            raise ValueError("Операция невозможна. Счет закрыт")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            self.history.pop()
            target_account.history.pop()
            op=Operation(-amount,amount*Account.FEE,self.name)
            self.history.append(op)
            op = Operation(amount, source=self.name)
            target_account.history.append(op)

    def deposit(self, amount):
        if self.in_archive:
            raise ValueError("Операция невозможна. Счет закрыт")
        else:
            self.balance += amount
            op=Operation(amount)
            self.history.append(op)

    def withdraw(self, amount):
        if self.in_archive:
            raise ValueError("Операция невозможна. Счет закрыт")
        else:
            if self.balance >= amount*(1+Account.FEE):
                self.balance -= amount*(1+Account.FEE)
                op = Operation(-amount,amount*Account.FEE)
                self.history.append(op)
            else:
                raise ValueError("Недостаточно средств на счете")

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."

    def show_history(self):
        for el in self.history:
            print(el)


    # TODO: добавляем комиссию
    #  и переход/восстановление их архива. Свойство: in_archive --> True, если аккаунт в архиве, и False - если нет
    def to_archive(self):
        """
        Переводим аккаунт в архив
        """
        self.in_archive=True

    def restore(self):
        """
        Восстанавливаем из архива
        """
        self.in_archive=False


account1 = Account("Иван", "1122 523632", "+7-900-200-02-03")
# print(account1)
# print(account1.full_info())
account1.deposit(100)
# print(account1)
account1.withdraw(50)
# print(account1)
account2 = Account("Вася", "3344 123456", "+7-911-156-25-78", 1000)
account1.transfer(account2, 30)
account3 = Account("Галя", "3344 123456", "+7-911-156-25-78", 200)
# print(account1)
# print(account2)
account3.transfer(account1, 100)
#account1.show_history()
#print(account1)
account1.to_archive()
account1.restore()
account1.deposit(100)
print(account1)

