# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.


def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

def sort_choice_m(nums):
    i = 0
    count = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            count += 1
            if abs(nums[j]) < abs(nums[m]): # такая сортировка по модулю
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

c=24
num = gen_list(c)
sum_ = 0
print(f'before sort ', num)
sort_choice_m(num)
print(f'after sort by mod ', num)
num_ = num[c-10:]
for el in num_:
        sum_ += el
print(f'Sum = ',sum_)
