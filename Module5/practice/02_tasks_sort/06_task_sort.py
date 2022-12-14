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

goods_price = [2, 1, 10, 50, 100, 70, 25, 56, 36, 99,30]
max_check_sum = 0

i = 0
while i < len(goods_price) - 1:
    j = i + 1
    while j < len(goods_price):
        m = i
        if goods_price[j] > goods_price[m] and m % 2 == 0:
            m = j
            goods_price[i], goods_price[m] = goods_price[m], goods_price[i]
        elif goods_price[j] < goods_price[m] and m % 2 != 0:
            m = j
            goods_price[i], goods_price[m] = goods_price[m], goods_price[i]
        j += 1
    i += 1

i = 0    
while i < len(goods_price):
    max_check_sum += goods_price[i]
    i += 2

print(max_check_sum)
