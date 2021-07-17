import math
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

def gen_list(size, at=0, to=100):
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    import random
    num_list = []
    for _ in range(size):
        num_list.append(random.randint(at, to))
    return num_list

price = gen_list(1000)
price.sort(reverse = True)
half_index = math.ceil(len(price)/2)
print(sum(price[-half_index:]))

# staff.sort(key = lambda emp: (emp["salary"], emp["surname"]))
# 
# res = sum(map(lambda emp: emp["salary"], staff[:3]))
# print(res)

# sum_salary = 0
# for emp in staff[:3]:
#     sum_salary += emp["salary"]
# print(res)

# print("Список сотрудников отсортированный по уменьшению ЗП:", staff)
# print("Список сотрудников отсортированный по уменьшению ЗП:", sort_staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
