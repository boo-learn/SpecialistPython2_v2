# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.

def bubble_sort(nums):
    count = 0
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            count += 1
            # print("i = ", i)
            if abs(nums[i]) > abs(nums[i + 1]):
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    # print("count = ", count)

def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


nums = gen_list(10)
bubble_sort(nums)

print(nums)

result = 0
for num in nums[-5:]:
    result += abs(num)
print(sum(nums[-5:]))
