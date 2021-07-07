# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
def gen_list(size, at=-100, to=100):
    import random
    random_list = []
    for i in range(size):
        random_list.append(random.randint(at, to))
    return random_list
  
  
def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums

  
def summary_list(my_list):
    summary = 0
    maxinlist = my_list[-10:]
    for elem in maxinlist:
        summary += elem
    return summary

random_list = gen_list(100)
sorted_list = bubble_sort(random_list)
print(summary_list(sorted_list))
