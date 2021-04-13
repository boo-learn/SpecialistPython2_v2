class Account(AccountBase):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        super().__init__(name, passport8, phone_number, start_balance)
        self.history = {'withdraw': [], 'deposite': [], 'transfer': []}

    def to_history(self, action):
        if action.split[0] == 'withdraw':
            self.history[action.split()[0]] += [f'Снято со счета {action.split()[1]}, остаток {self.balance}']
        elif action.split[0] == 'deposite':
            self.history[action.split()[0]] += [f'Зачислено на счет {action.split()[1]}, остаток {self.balance}']
        elif action.split[0] == 'transfer':
            self.history[action.split()[0]] += [f'Переведено на другой счет {action.split()[1]}, остаток {self.balance}']

    def from_history(self):
        out = ''
        for v in self.history.values():
            for action in v:
                out += action + '\n'
        return out

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount)
        target_account.deposite(amount)
        self.to_history(f'transfer {amount}')

    def deposite(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        self.to_history(f'deposite {amount}')

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if amount > self.balance:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.to_history(f'withdraw {amount}')

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс: {self.balance}. Паспорт: {self.passport8}. тел.: {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance}."
