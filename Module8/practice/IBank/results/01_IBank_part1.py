# Сюда отправляем готовое решение IBank часть-1
class Account(AccountBase):
        def transfer(self, target_account, amount):
            """
            Перевод денег на счет другого клиента
            :param target_account: счет клиента для перевода
            :param amount: сумма перевода
            :return:
            """
            pass


        def deposit(self, amount):
            if amount < 0:
                raise ValueError ("Только положитетельная сумма")
            self.balance += amount


        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount



        def full_info(self):
            return f'{self.name} баланс {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}'

        def __repr__(self):
            return f"{self.name} баланс: {self.balance} руб."
