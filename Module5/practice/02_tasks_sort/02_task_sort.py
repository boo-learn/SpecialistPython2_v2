# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов вдиапазоне at..to 
    """
    random_list = [random.randint(at, to) for i in range(size)]
    return random_list

gen = gen_list(100)
A = -50
B = -40
summa = 0
for i in gen:
    if i > A and i < B:
        summa += i

print(summa)
