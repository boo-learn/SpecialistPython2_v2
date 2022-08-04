from typing import List
# Сюда отправляем готовое решение IBank часть-2

# класс для хранение информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, ):
        # TODO: Тут добавляем свойства для хранение информации об операции
        pass

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        pass


class Account:
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: историю храним как список объектов класса Operation, добавив свойство в конструктор:
    #   self.__history = []

    # Данный метод дан в готовом виде. Изучите его и используйте как пример, для доработки других
    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            self.__history.append(Operation(amount, Operation.DEPOSIT))

    def get_history(self) -> List[str]:
        """
        :return: возвращаем историю операций  виде списка строковых представлений
        """
        return [str(operation) for operation in self.__history]
