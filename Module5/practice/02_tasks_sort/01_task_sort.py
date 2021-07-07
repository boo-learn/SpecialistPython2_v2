# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

def gen_list(size, at=0, to=100):
    from random import randint
    num = []
    for _ in range(size):
        num.append(randint(at, to))
    return num


a = 35
li = gen_list(20)
new = []
i = 0
for i in range(len(li)):
    if li[i] > a:
        new.append(li[i])
summa = sum(new)
print(new)
print(summa)
