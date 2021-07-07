# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
import math
def gen_list(size, at=-100, to=100):
    import random
    random_list = []
    for i in range(size):
        random_list.append(random.randint(at, to))
    return random_list
  

def bubble_sortabs(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if abs(nums[i]) > abs(nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums
  
  
random_list = gen_list(100)
sorted_abslist = bubble_sortabs(random_list)
print(summary_list(sorted_abslist))
