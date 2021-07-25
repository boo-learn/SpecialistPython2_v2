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

list_of_products = [int(i) for i in input(': ').split()]
sorted(list_of_products, reverse=True)
trick_list = []
index_count = 1
cheap = sorted(list_of_products[:int(len(list_of_products) / 2)])
expensive = sorted(list_of_products[int(len(list_of_products) / 2):])

che_count = 0
exp_count = 0
for i in range(int(len(list_of_products))):
    if i % 2 == 0:
        trick_list.append(cheap[che_count])
        che_count += 1
    else:
        trick_list.append(expensive[exp_count])
        exp_count += 1

print(trick_list)
print(sum(expensive))
