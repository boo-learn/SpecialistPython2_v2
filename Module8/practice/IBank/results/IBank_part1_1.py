class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"..."

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"..."


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34")
print(account1)  # При отсутствии .__str__(), вызывает __repr__()
print(account1.full_info())

account2 = Account(name="Алексей", phone_number="+7-901-744-22-99", passport="3232 456124", start_balance=500)
print(account2)  # При отсутствии .__str__(), вызывает __repr__()
print(account2.full_info())
