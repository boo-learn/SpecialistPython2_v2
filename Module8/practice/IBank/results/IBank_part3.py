# Сюда отправляем готовое решение IBank часть-2

class Operation:
    # класс для хранение информации об операциях
    DEPOSIT = 'пополнение'
    WITHDRAW = 'списание'
    TRANSFER = 'перевод'
    INCOME = 'поступление'
    def __init__(self, type, amount, target_account=None, fee=0):
        self.type = type
        self.amount = amount
        self.target_account = target_account
        self.fee = fee

    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        base_str = f'{self.type} {self.amount} руб.'
        if self.target_account is not None:
            base_str += f'на счет клиента: {self.target_account.name}'
        if self.fee:
            base_str += f' (комиссия: -{self.fee})'
        return base_str


# Сюда отправляем готовое решение IBank часть-3
class Account:
    FEE = 2
    def __init__(self, name, passport, phone_number, start_balance=0, in_archive=False):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance
        self.__history = []
        self.in_archive = in_archive

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if not self.in_archive:
            self.withdraw(amount, record=False)
            target_account.deposit(amount, record=False)
            op = Operation(Operation.TRANSFER, amount, target_account, fee=round(Account.FEE/100 * amount))
            self.__history.append(op)

            op = Operation(Operation.INCOME, amount, self)
            target_account.__history.append(op)
        else:
            raise Exception('Операция невозможна. Счет закрыт.')

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if not self.in_archive:
            self.balance += amount
            if record:
                op = Operation(Operation.DEPOSIT, amount)
                self.__history.append(op)
        else:
            raise Exception('Операция невозможна. Счет закрыт.')

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if not self.in_archive:
            fee = Account.FEE/100 * amount
            if self.balance < fee + amount:
                raise ValueError('Недостаточно средств для проведения операции')
            self.balance -= (fee + amount)
            if record:
                op = Operation(Operation.WITHDRAW, amount, fee=round(fee))
                self.__history.append(op)
        else:
            raise Exception('Операция невозможна. Счет закрыт.')

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

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        hist_str = ''
        for op in self.__history:
            hist_str += str(op) + '\n'
        return hist_str
    #  и переход/восстановление их архива. Свойство: in_archive --> True, если аккаунт в архиве, и False - если нет
    def to_archive(self):
        """
        Переводим аккаунт в архив
        """
        self.in_archive = True
        self.balance = 0


    def restore(self):
        """
        Восстанавливаем из архива
        """
        self.in_archive = False

