# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.
import random
def gen_list(size, at=-100, to=100):

    nums = []
    for i in range(size):
        nums.append(random.randint(at, to))
    return nums

nums = gen_list(5)
print(nums)
less_num = random.randint(-100, 100)
more_num = random.randint(-100, 100)
while less_num >= more_num:
    less_num = random.randint(-100, 100)
print(less_num, more_num)

sum_nums = 0
for num in nums:
    if less_num < num < more_num:
        sum_nums += num

print(sum_nums)
