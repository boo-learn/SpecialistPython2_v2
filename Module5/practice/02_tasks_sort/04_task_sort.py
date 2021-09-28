# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]



def sort_choice(nums:list):
    # nums = [5, 2, -1, 8, 4, -4, 7]
    # print("before sort = ", nums)
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    # print("after sort = ", nums)

numbers_abs = []
for number in numbers:
    numbers_abs.append(abs(number))

# print(numbers_abs)
sort_choice(numbers_abs)
# print(numbers_abs)

summa_abs = 0
for number_abs in numbers_abs[-5:]:
    # print(number_abs)
    for number in numbers:
        if number_abs == abs(number):
            # print(number)
            summa_abs += number


print(summa_abs)
