# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
bubble_sort(numbers)
print(sum(numbers[:5:-1]))
