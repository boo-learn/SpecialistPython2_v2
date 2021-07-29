# Сюда отправляем готовое решение IBank часть-3
class Operation:
    # класс для хранение информации об операциях
    DEPOSIT = "пополнение"
    WITHDRAW = "списание"
    TRANSFER = "перевод"
    INCOME = "поступление"

    def __init__(self, type, amount, target_account=None, fee=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.fee = fee

    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        base_str = f"{self.type} {self.amount} руб."
        if self.target_account:
            base_str += f' на счет клиента: {self.target_account.name}'
        if self.fee:
            base_str += f' (коммиссия: {self.fee} руб)'
        return base_str


class Account:
    FEE = 2

    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance
        self.__history = []
        self.in_archive = False

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, record=False)
        target_account.deposit(amount, record=False)

        op = Operation(Operation.TRANSFER, amount, target_account, fee=int(amount * (self.FEE / 100)))
        self.__history.append(op)

        op = Operation(Operation.INCOME, amount, self)
        target_account.__history.append(op)

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        if record:
            op = Operation(Operation.DEPOSIT, amount)
            self.__history.append(op)

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        if record:
            op = Operation(Operation.WITHDRAW, amount)
            self.__history.append(op)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        hist_str = ""
        for op in self.__history:
            hist_str += str(op) + "\n"
        return hist_str

    def to_archive(self):
        """
        Переводим аккаунт в архив
        """
        self.in_archive = True

    def restore(self):
        """
        Восстанавливаем из архива
        """
        self.in_archive = False

    account1 = Account("Иван", "3445 123456", "+7-900-600-11-22")
    account2 = Account("Алекс", "3445 123426", "+7-900-600-11-33")
    account1.deposit(500)
    account1.withdraw(100)
    try:
        account1.transfer(account2, 200)
    except ValueError as e:
        print(e)
    print(account1.show_history())
    print("**********")
    print(account2.show_history())

    # print(account2)

    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: добавляем комиссию
    #  и переход/восстановление их архива. Свойство: in_archive --> True, если аккаунт в архиве, и False - если нет
