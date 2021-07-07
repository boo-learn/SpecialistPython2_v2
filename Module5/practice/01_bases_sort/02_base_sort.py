# Все алгоритмы сортировки из examples/ оберните в функции


def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums

def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    return (nums)


def quick_sort(nums):
    pass
    

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    random_list = []
    for i in range(size):
        random_list.append(random.randint(at, to))
    return random_list
    # """
    # :param size: кол-во элементов списка
    # :param at: минимально возможное значение элементов
    # :param to: максимально возможное значение элементов
    # :return: списко из size произвольных элементов вдиапазоне at..to
    # """
random_list = gen_list(25, -50, 35)
print(random_list)
print(bubble_sort(random_list))
print(sort_choice(random_list))
