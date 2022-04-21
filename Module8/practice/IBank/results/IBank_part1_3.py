class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance

    def transfer(self, target_account, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            target_account.__balance += amount
        else:
            return ValueError("Недостаточно средств")


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

try:
    account1.transfer(account2, 500)
except ValueError as e:
    print(e)
print(account1)
print(account2)

try:
    account1.transfer(account2, 600)
except ValueError as e:
    print(e)
print(account1)
print(account2)

