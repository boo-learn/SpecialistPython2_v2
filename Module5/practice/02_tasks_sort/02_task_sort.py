# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.
import random
def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = random.uniform(-30,30)  # Задайте самостоятельно, выбрав произвольное число
b = random.uniform(a+1,30)  # Задайте самостоятельно, выбрав произвольное число
print(f" До сортировки:{numbers}")
sort_choice(numbers)
print(f" После сортировки:{numbers}")
print(f"{a=}  {b=}" )
sum = float(0)
for _ in range(len(numbers) - 1):

    if a < numbers[_] < b:
        #print(numbers[_])
        sum +=numbers[_]
print(sum)
