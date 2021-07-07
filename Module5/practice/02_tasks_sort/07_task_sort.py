# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
import random

def max_сheque(list_prices):
    import math
    mc = 0
    list_prices.sort(reverse=True)
    l = len(list_prices)
    expensive = list_prices[:math.ceil(l/2)]
    cheap = list_prices[math.ceil(l/2):]
    print(expensive)
    print(cheap)
    return sum(expensive)

N = 21
array = [random.randint(1, 1000) for _ in range(N)]
print(array)
print(f"Max cheque sum is {max_сheque(array)}")
