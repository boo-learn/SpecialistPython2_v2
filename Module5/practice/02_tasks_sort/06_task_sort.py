# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые  баллы  получают дипломы  одинаковой степени.
# Призером олимпиады считается участник, получивший диплом  не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5

import random


def bubble_sort(nums, key=lambda x: x, reverse=False):
    count = 0
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                count += 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    # print(f'{count=}')


def gen_list(size, at=-100, to=100):
    import random
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


grades = gen_list(random.randint(1, 100), 1, 10)
bubble_sort(grades, reverse=True)
print(grades)

prev_grade = grades[0]
steps = 0
num_peoples = 0
for grade in grades:
    if grade < prev_grade:
        steps += 1
        prev_grade = grade
    if steps > 2:
        break
    num_peoples += 1
print(num_peoples)
