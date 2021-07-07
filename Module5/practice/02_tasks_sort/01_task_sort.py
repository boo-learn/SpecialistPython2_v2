# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

def gen_list(size):
    import random
    return [random.randint(-100, 100) for _ in range(size)]

a = 60
num = gen_list(10)
print(num)
sum = 0
for i in num:
    if i > a:
        sum = sum + i
print(sum)
