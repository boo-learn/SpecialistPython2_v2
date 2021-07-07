# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
def gen_list(size, at=0, to=20):
    from random import randint
    num = []
    for _ in range(size):
        num.append(randint(at, to))
    print("Исходный список: ", num)
    return num


def bubble_sort(nums):
    print("before sort = ", nums)
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    return nums


li = gen_list(20)
bub = bubble_sort(li)
print("after sort = ", bub)
summa = sum(li[-10::])
print(f"Сумма чисел : ", summa)
