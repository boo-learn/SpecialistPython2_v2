# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]


def sort_choice(nums: list, reverse: bool = False) -> None:

    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                condition = nums[j] > nums[m]
            else:
                condition = nums[j] < nums[m]
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


sort_choice(numbers)
sum_max_5 = sum(numbers[:5])
print(numbers)
