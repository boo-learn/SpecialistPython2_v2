class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance

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

    def add_money(self, money_quantity: int):
        self.balance += money_quantity

    def get_money(self, money_quantity: int) -> bool:
        if money_quantity <= self.balance:
            self.balance -= money_quantity
            return True
        else:
            raise ValueError("Денег на счету недостаточно")

    def transfer_money(self, other_client, money_quantity):
        if self.get_money(money_quantity):
            other_client.balance += money_quantity


# account1 = Account("Иван", "3230 634563", "+7-900-765-12-34")
# print(account1)  # При отсутствии .__str__(), вызывает __repr__()
# print(account1.full_info())
#
# account2 = Account(name="Алексей", phone_number="+7-901-744-22-99", passport="3232 456124", start_balance=500)
# print(account2)  # При отсутствии .__str__(), вызывает __repr__()
# print(account2.full_info())

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 5000)
account1.get_money(500)
print(account1)  # При отсутствии .__str__(), вызывает __repr__()
print(account1.full_info())
