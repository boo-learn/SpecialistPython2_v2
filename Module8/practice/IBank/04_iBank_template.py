class Account(AccountBase):
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance < amount:
            raise ValueError("Суммы на счёте недостаточно")
        target_account.balance += amount
        self.balance -= amount

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount < 0:
            raise ValueError("Сумма должна быть положительная")
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError("Суммы на счёте недостаточно")
        self.balance -= amount

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name}  баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """

        return f"{self.name} баланс: {self.balance} руб."
