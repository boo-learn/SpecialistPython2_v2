# Сюда отправляем готовое решение IBank часть-4
class Operation:
    # TODO-0: сюда копируем реализацию класса Operation из предыдущей задачи
    pass


class Account:
    pass
    # TODO-0: сюда копируем реализацию класса Account из предыдущей задачи


# TODO-1: Создаем класс для кредитного аккаунта, наследуясь от аккаунта
class CreditAccount(Account):
    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        # TODO-1: Пока реализуем ТОЛЬКО первый пункт задания "возможность уходить в отрицательный баланс"
        #   Договоримся, что negative_limit будет положительным числом.
        #   Например, negative_limit = 500 означает, что мы можем уйти в минус на 500 рублей, self.__balance = -500
        pass
