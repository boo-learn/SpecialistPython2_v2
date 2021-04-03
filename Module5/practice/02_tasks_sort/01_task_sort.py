# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А
import random
def gen_list(size, at=-100, to=100):

    nums = []
    for i in range(size):
        nums.append(random.randint(at, to))
    return nums

nums = gen_list(15)
print(nums)
more_num = random.randint(-100, 100)
print(more_num)

sum_nums = 0
for num in nums:
    if num > more_num:
        sum_nums += num

print(sum_nums)

