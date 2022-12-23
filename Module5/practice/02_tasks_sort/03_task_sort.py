# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов
def top_bubble(nums, size):
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
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    print(nums[len(nums) - size:])
    return nums[len(nums) - size:]


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
size = 5
print(sum(top_bubble(numbers, size)))
