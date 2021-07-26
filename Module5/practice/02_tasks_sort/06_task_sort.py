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

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        j = 0
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
            j += 1


def gen_list(size, at=1, to=100):
    return [random.randint(at, to) for _ in range(size)]


# num_products = int(input("Общее колличество товаров:")) # Можно создать рандомный список с любым количеством товаров для сверки
# products_list = gen_list(num_products)

products_list = [5, 2, 1, 10, 50, 10]               # Нужно закомментировать при включении пункта выше (строчки 36-37)
print(f"Общее колличество товаров:{products_list}") # Нужно закомментировать при включении пункта выше (строчки 36-37)

n = int(input("Колличество купленных товаров:"))

bubble_sort(products_list)
k = len(products_list) // 2
cheap = list(products_list[:k])
expensive = list(products_list[k:])
event = []
sum_expensive = 0
for i in range(n):
    if i % 2 == 0:
        event.append(random.sample(expensive, 1))
    else:
        event.append(random.sample(cheap, 1))

event_list = list(map(lambda x: x[0], event))

sum_expensive = []
for i in range(len(event_list)):
    if i % 2 == 0:
        sum_expensive.append(event_list[i])
        
print(f"Цены дешевых товаров{cheap}")           #Вывод только для сверки
print(f"Цены дорогих товаров{expensive}")       #Вывод только для сверки
print(f"Список покупок на акции {event_list}")  #Вывод только для сверки
print(f"Максимальная сумма чека {sum(sum_expensive)} руб.")

