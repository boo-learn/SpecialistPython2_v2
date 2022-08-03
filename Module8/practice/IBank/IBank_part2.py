import re

class Operation:
    # класс для хранение информации об операциях
    def __init__(self, oper_type: str, amount: int, name: str = ''):
        # Тут добавляем свойства для хранение информации об операции
        self.type = oper_type
        self.amount = amount
        self.client = name


    def __repr__(self) -> None:
        """
        :return: возвращает строковое представление операции
        """
        return f'{self.type} {self.amount} руб.'

class Account:

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance
        passport_pattern = r"\d{4} \d{6}"
        phone_pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if not re.match ( passport_pattern, self.passport ):
            raise ValueError ( f'Неверный формат паспорта для клиента {self.name}' )
        if not re.match ( phone_pattern, self.phone_number ):
            raise ValueError ( f'Неверный формат телефона для клиента {self.name}' )
        self.__history = []

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        self.__history.append(Operation('Пополнение', amount))

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance - amount < 0:
            raise ValueError ('Сумма не может быть отрицательной')
        else:
            self.__balance -= amount
            self.__history.append(Operation('Снятие', amount))

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.__balance - amount < 0:
            raise ValueError ( 'Сумма не может быть отрицательной' )
        elif self.__balance < amount:
            raise ValueError ( 'На счету нет запрошенной суммы' )
        else:
            self.__balance -= amount
            target_account.__balance += amount
            self.__history.append(Operation(f'Перевод на счет клиента {target_account.name}', amount))
            self.__history.append(Operation(f'Поступление со счета клиента {self.name}', amount))

    def show_history(self) -> str:
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        for item in self.__history:
            print(item)

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "3232 456124", "+7-901-365-18-76", 200)


account1.deposit(100)
account2.deposit(500)

account1.withdraw(350)
account2.withdraw(100)

account1.transfer(account2, 300)
account2.transfer(account1, 100)

#печатаем историю операций

account1.show_history()
account2.show_history()
