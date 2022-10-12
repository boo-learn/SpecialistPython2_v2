



def bubble_sort(nums):
    swapped = True
    n = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        n += 1


# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
n=5
bubble_sort(numbers)
print(numbers)
print(sum(numbers[len(numbers)-n+1:]))
