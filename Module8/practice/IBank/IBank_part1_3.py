class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance

    def full_info(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        return f"{self.name} баланс: {self.__balance} руб."
    
    def transfer(self, target_account: 'Account', amount: int) -> None:
        if type(amount) == int and amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                target_account.deposit(amount)
            else:
                raise ValueError("Операция не выполнена! Не дсотаточно средств!")
        else:
            raise ValueError("Операция не выполнена! только положительные целые числа!")    

    
    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        if type(amount) == int and amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                raise ValueError("Операция не выполнена! Не дсотаточно средств!")
        else:
            raise ValueError("Операция не выполнена! только положительные целые числа!")
