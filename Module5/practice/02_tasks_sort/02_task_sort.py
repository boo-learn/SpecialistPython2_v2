# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

def gen_list(size):
    import random
    return [random.randint(-100, 100) for _ in range(size)]

a = 60
b = 80
num = gen_list(10)
print(num)
sum = 0
for i in num:
    if i > a and i < b:
        sum = sum + i
print(sum)
