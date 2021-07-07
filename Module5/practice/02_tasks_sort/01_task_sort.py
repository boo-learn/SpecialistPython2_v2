# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
def sum_more(num_list: list, a):
    total = 0
    for num in num_list:
        if num > a:
            total += num
    return total


print(sum_more([random.randrange(-50, 50) for _ in range(0, 1000000)], 4))
