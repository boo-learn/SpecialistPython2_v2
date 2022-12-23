# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

def top_abs_bubble(nums, size):
    """
    :param nums: список чисел
    :param size: количество возвращаемых самых больших чисел
    :return: список из size самых больших чисел из списка nums
    """
    if size > len(nums):
        size = len(nums)
    swapped = True
    j = 0
    while swapped and j <= size:  # сортриуем методом пузырька, но только до размера size
        j += 1
        swapped = False
        for i in range(len(nums) - j):
            if abs(nums[i]) > abs(nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    print(nums[len(nums) - size:])
    return nums[len(nums) - size:]


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
size = 2
print(sum(top_abs_bubble(numbers, size)))
