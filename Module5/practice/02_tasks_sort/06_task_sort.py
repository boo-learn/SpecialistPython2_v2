

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

lst = [10, 2, 50, 1, 10]
if len(lst)%2 == 0:
    lst.sort()
    print(sum(lst[int(len(lst)/2):]))
else:
    lst.sort()
    print(sum(lst[int(len(lst) / 2):]))
