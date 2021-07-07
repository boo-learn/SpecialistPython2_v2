# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
def gen_list(size, at=0, to=10):
    from random import randint
    num = []
    for _ in range(size):
        num.append(randint(at, to))
    print("Исходный список: ", num)
    return num


a = 3
b = 9
li = gen_list(10)
new = []
i = 0
for i in range(len(li)):
    if li[i] > a:
        if li[i] < b:
            new.append(li[i])
summa = sum(new)
print("Проверяем новый список: ", new)
print(f"Сумма чисел больших {a} и меньших {b}: ", summa)
