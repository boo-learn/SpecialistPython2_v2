# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.

def bubble_sort(nums):
    j = 0
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - j - 1):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    return nums

def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов вдиапазоне at..to 
    """
    random_list = [random.randint(at, to) for i in range(size)]
    return random_list

gen = gen_list(100)
# gen_abs = [abs(el) for el in gen]
gen_abs = map(abs, gen)
gen_abs = list(gen_abs)
gen_abs_sort = bubble_sort(gen_abs)
print(sum(gen_abs_sort[-10:]))
