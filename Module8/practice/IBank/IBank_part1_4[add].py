import re

class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу
        pattern_passport = r"\d{4} \d{6}"
        pattern_phone = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
        if re.match(pattern_passport, passport):
            self.passport = passport
        else:
             raise ValueError('Неверный формат паспорта')

        if re.match(pattern_phone, phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError('Неверный формат телефона')

    def full_info(self) -> str:
        return f"{self.name} баланc: {self.balance}руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланc: {self.balance}руб."

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError('Недостаточно денег на счёте.')

    def transfer(self, target_account: 'Account', amount: int) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
            target_account.__balance += amount
        else:
            raise ValueError('Недостаточно денег на счёте для перевода.')

    # TODO-1: добавьте проверку паспорта и телефона(в конструкторе) на соответствие заданным форматам
    #  В случае несоответствия выбрасываем исключение ValueError("Неверный формат телефона/паспорта")
    #  Проверка информации на корректность - валидация
    #  Готовые валидаторы можете взять в директории helpers
    pass


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "3233 456124", "+7-901-744-22-99")  # номер паспорта задан неверно
account3 = Account("Петр", "3232 456124", "+7-904-745-47-3", 400)  # номер телефона задан неверно
