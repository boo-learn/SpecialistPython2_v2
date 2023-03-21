# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

def sort_choice(nums, reverse=False, abs_flag=False) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if abs_flag:
                if reverse:
                    rule_sort = abs(nums[j]) > abs(nums[m])
                else:
                    rule_sort = abs(nums[j]) < abs(nums[m])
            else:
                if reverse:
                    rule_sort = nums[j] > nums[m]
                else:
                    rule_sort = nums[j] < nums[m]
            if rule_sort:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

sort_choice(numbers, reverse=True, abs_flag=True)
print(sum(numbers[:5]))
