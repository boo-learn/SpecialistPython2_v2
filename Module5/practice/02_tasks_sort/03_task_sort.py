# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов


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


numbers = [-2.5, 1, -13, -22.4, -12.8, -6.7, -12.8, 1, 4, 1, 1]

bubble_sort(numbers)
i = 1
num_sum = 0
while i < 6:
    num_sum += numbers[-i]
    i += 1
print(num_sum)
