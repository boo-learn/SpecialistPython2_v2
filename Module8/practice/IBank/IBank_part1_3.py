class Account:
    # TODO-0: скопируйте реализацию из предыдущего решения

    # TODO-1: напишите реализацию метода transfer()
    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if target_account.__balance >= amount:
            target_account.__balance -=amount
            self.deposit(amount)
        else:
            raise ValueError("Недостаточно средств на счете")


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
try:
    account1.transfer(account2, 500)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)

# Переводим еще с первого аккаунт на второй:
try:
    account1.transfer(account2, 600)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)
