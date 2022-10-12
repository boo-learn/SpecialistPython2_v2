# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход:дано N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10


prices = [2, 1, 10, 50, 10, 4, 7]


prices.sort(reverse=True)

pair_amount = round(len(prices)/2)

check = 0
for price in prices[:pair_amount]:
    check += price

print(f"Max Check: {check}")
