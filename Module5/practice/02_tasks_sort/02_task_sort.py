# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.

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
B = random.randint(A,10)
print ("B = ", B)

summ=0
for i in sp:
    if (i>A)and(i<B): summ+=i
print ("summ (B > list[] > A) = ", summ)
