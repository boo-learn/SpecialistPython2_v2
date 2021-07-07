# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

import random

def gen_list(size, at, to):
    s=[]
    for _ in range(size):
        s.append(random.randint(at,to))
    return s

sp=gen_list(10,0,10)
print ("list = ",sp)
A = random.randint(0,10)
print ("A = ", A)
summ=0
for i in sp:
    if i>A: summ+=i
print ("summ (list[] > A) = ", summ)
