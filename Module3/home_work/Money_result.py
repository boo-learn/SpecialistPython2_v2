class Money:
    def __init__(self, rubles, kopecks):
        self.__kopecks = (rubles * 100) + kopecks

    @staticmethod
    def __resolve_negative_sum(_kopecks: int):
        if _kopecks < 0:
            rubles = abs(_kopecks) // 100
            kopecks = abs(_kopecks) % 100
            return Money(-rubles, kopecks)
        else:
            rubles = _kopecks // 100
            kopecks = _kopecks % 100
            return Money(rubles, kopecks)

    def __str__(self):
        rubles = self.__kopecks // 100
        kopecks = self.__kopecks % 100
        return f'{rubles}руб {kopecks}коп'

    def __add__(self, other):
        _kopecks = self.__kopecks + other.__kopecks
        return self.__resolve_negative_sum(_kopecks)

    def __sub__(self, other):
        _kopecks = self.__kopecks - other.__kopecks
        return self.__resolve_negative_sum(_kopecks)


# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп
