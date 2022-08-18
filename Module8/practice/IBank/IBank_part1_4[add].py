import re

class Account:

        # TODO-1: добавьте проверку паспорта и телефона(в конструкторе) на соответствие заданным форматам
    #  В случае несоответствия выбрасываем исключение ValueError("Неверный формат телефона/паспорта")
    #  Проверка информации на корректность - валидация
    #  Готовые валидаторы можете взять в директории helpers
    patternforphone = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"
    patternforpassport=r"\d{4} \d{6}"
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу
     

    def full_info(self) -> str:
      
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
      
        return f"{self.name} баланс: {self.balance} руб."
    def validatephone(self):
        
        if  re.match(Account.patternforphone, self.phone_number):
            print(f"Номер телефона {self.phone_number} корректный")
        else:
            print(f"Номер телефона {self.phone_number} не корректный")


            #????????
    def validatepassport(self):
        
        if  re.match(Account.patternforpassport, self.passport):
            print(f"Номер паспорта  корректный")
        else:
            print(f"Номер паспорта  не корректный")


    
    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
       
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
      
        if self.__balance < amount:
            raise ValueError("У Вас не достаточно средств...")

        self.__balance -= amount


            # TODO-1: напишите реализацию метода transfer()
    def transfer(self, target_account: 'Account', amount: int) -> None:
     
        if self.__balance < amount:
            raise ValueError("У Вас не достаточно средств...")
        else:
            target_account.__balance+=amount
            self.__balance-=amount
        




# Создаем тестовый аккаунт:
#account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", start_balance=500)
#print(account1.balance)
# Смотрим баланс:
#print(account1)

# Вносим сумму на счет:
#account1.deposit(600)
#print(account1)

# Снимаем деньги со счета:
#try:
 #   account1.withdraw(1000)
#except ValueError as e:
 #   print(e)
#print(account1)

# Пробуем снять еще:
#try:
    #account1.withdraw(1000)
#except ValueError as e:
  #  print(e)
#print(account1)

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
try:
    account1.transfer(account2, 500)
except ValueError as e:
    print(e)

print("Проверяем изменения баланса:")
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


#phone_numbers = ["+7-900-620-10-20", "8-900-620-10-20", "+7-90-62-10-20", "+7 900 620 10 20", "+7-100-100-11-22"]
#pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

#for phone_number in phone_numbers:
   # if re.match(pattern, phone_number):
    #    print(f"Passport number {phone_number} is correct")
    #else:
      #  print(f"Passport number {phone_number} is not correct")

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно


account1.validatephone()
account1.validatephone()
account2.validatephone()
account2.validatepassport()
account3.validatepassport()
account3.validatepassport()
