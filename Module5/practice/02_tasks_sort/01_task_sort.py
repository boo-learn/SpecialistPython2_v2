# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
def gen_list(size, at=-100, to=100):
    import random
    list1 = []
    for _ in range(size):
        k = random.randint(at,to)
        list1.append(k)
    return list1
k = gen_list(5)

A = 0
summ = 0
for i in k:
    if i > A:
        summ += i
print(k)
print(f'сумма элементов больше {A}={summ}')
