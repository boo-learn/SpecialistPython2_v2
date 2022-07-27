# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]


def bubble_sort(list: list):
    j = 1
    nums = list
    # print("before sort = ", nums)
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    # print("after sort = ", nums)
    return nums


bubble_sort(numbers)
numbers_min = numbers[:5]
numbers_max = numbers[:4:-1]
print(numbers_min)
print(numbers_max)
i = 0
summ = 0
while i < 5:
    if abs(numbers_max[i]) >= abs(numbers_min[i]):
        summ += numbers_max[i]
    else:
        summ += numbers_min[i]
    i += 1
print(summ)
