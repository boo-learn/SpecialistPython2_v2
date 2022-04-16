# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]


def bubble_sort_abs(nums):
    n = 0
    swapped = True
    while swapped:
        swapped = False
        n += 1
        for i in range(len(nums) - n):
            if abs(nums[i]) > abs(nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


bubble_sort_abs(numbers)
summ = sum(numbers[len(numbers) - 5:])
print(summ)
