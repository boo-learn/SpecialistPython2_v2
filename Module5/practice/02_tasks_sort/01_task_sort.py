# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А

def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

num = gen_list(100)
A=34
sum_ = 0
i=0
#print(num)
for i in range(len(num)):
    if num[i]>A:
        sum_ += num[i]
        i += 1
print(sum_)
