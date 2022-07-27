# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3
def bubble_sort(nums):
    swapped = True
    cnt = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - cnt):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        cnt += 1


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
abs_numbers = list(map(abs, numbers))
bubble_sort(abs_numbers)
max_abs_numbers = abs_numbers[-5:]
summa = round(sum(list(filter(lambda x: abs(x) in max_abs_numbers, numbers))), 1)
print(summa)
