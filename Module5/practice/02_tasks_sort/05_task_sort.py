# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
def sum_ten_greater(nums: list):
    swapped = True
    j = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - j):
            if abs(nums[i]) > abs(nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return sum(nums[-10:])


print(sum_ten_greater([random.randrange(-50, 50) for _ in range(0, 100)]))
