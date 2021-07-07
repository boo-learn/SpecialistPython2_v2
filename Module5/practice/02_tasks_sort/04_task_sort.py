# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
def gen_list(size, at=-100, to=100):
    import random
    list1 = []
    for _ in range(size):
        k = random.randint(at,to)
        list1.append(k)
    return list1
k = gen_list(15)
k_copy = k
print(k)
k_abs=[]
for i in k:
    k_abs.append(abs(i))
print(k_abs)
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return (nums)


summ = 0
k_abs_sort = bubble_sort(k_abs)
print(k_abs_sort)

for i in range(len(k_abs_sort)-1, len(k_abs_sort)-3, -1):
    if k_abs_sort[i] in k_copy:
        summ += k_abs_sort[i]
    else:
        summ -= k_abs_sort[i]
    # k_copy[:-1]

print(f'сумма элементов {summ}')
