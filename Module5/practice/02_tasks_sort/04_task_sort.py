# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3
def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        j += 1
        for i in range(len(nums) - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
def bubble_sort_abs(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        j += 1
        for i in range(len(nums) - j):
            if abs(nums[i]) > abs(nums[i + 1]):
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
bubble_sort_abs(numbers)
print(numbers)
i = 1
num_sum = 0
while i < 6:
    num_sum += numbers[-i]
    i += 1
print(num_sum)
