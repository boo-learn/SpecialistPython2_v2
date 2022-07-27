# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

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

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
sorted_nums = bubble_sort(numbers)
print(sorted_nums)
#print(sorted_nums[:-6:-1])
print(sum(sorted_nums[:-6:-1]))
