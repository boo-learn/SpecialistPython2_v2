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
def max_economy(quantity, goods):
    goods_econ = []
    goods.sort()
    goods_tall = goods[quantity // 2:]
    goods_free = goods[:quantity // 2]
    for i in range(len(goods_free)):  # это все делается для формирования списка, который в задании то и не требуется
        goods_econ.append(goods_tall[i])
        goods_econ.append(goods_free[i])
    goods_econ.extend(goods_tall[(len(goods_free)):])
    return sum(
        goods_tall)  # для выхода вообще достаточно return sum(goods[quantity//2:]), можно в одну строку записать
    # через ->


print(max_economy(5, [2, 1, 10, 50, 10]))
