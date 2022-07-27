# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

def bubble_sort(nums):
    #print("before sort = ", nums)
    swapped = True
    j = len(nums)-1
    while swapped:
        swapped = False
        for i in range(j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j -=1
    return nums

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

abs_numbers = [abs(num) for num in numbers] #bubble_sort(abs(numbers))
sorted_abs_numbers_5 = bubble_sort(abs_numbers)[-5:]
print('sorted_abs_numbers_5 = ', sorted_abs_numbers_5)
summa = sum(list(filter(lambda num: abs(num) in sorted_abs_numbers_5, numbers)))
print('summa=',summa)
