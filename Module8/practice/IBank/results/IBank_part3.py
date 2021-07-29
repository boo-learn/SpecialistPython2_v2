class Operation:
    # класс для хранение информации об операциях
    DEPOSIT = "Пополнение"
    WITHDRAW = "Списание"
    TRANSFER = "Перевод"
    INCOME = "Поступление"


    def __init__(self, type, amount, target_account=None, fee=0):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.fee = fee

        # Тут добавляем свойства для хранение информации об операции

    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        base_str = f"{self.type} {self.amount} руб."
        if self.target_account is not None:
            base_str += f"на счет клиента {self.target_account and self.target_account.name} комиссия составила {self.fee} руб."
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
        if self.in_archive or target_account.in_archive:
            raise ValueError("Операция невозможна. Счет закрыт")
        else:
            self.withdraw(amount, fee=int(amount * (self.FEE / 100)), record=False)
            target_account.deposit(amount, record=False)
            op = Operation(Operation.TRANSFER, amount, target_account, fee=-int(amount * (self.FEE / 100)))
            self.__history.append(op)
        

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        if record:
            op = Operation(Operation.DEPOSIT, amount)
            self.__history.append(op)

    def withdraw(self, amount,fee=0, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счету")

        amount += int(amount * (self.FEE / 100))
        self.balance -= amount
        if record:
            op = Operation(Operation.WITHDRAW, amount)
            self.__history.append(op)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """

        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        hist_str = ""
        for op in self.__history:
            hist_str += str(op) + "\n"
        return hist_str


    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: добавляем комиссию
    #  и переход/восстановление их архива. Свойство: in_archive --> True, если аккаунт в архиве, и False - если нет
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
