# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

nums = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

swapped = True
j = 1
while swapped:
    swapped = False
    # print("*****")
    for i in range(len(nums) - j):
        # print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
    j += 1
print(nums)
print(sum(nums[-5:]))
