def bubble_sort(nums) -> list:
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


def sort_choice(nums) -> list:
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
    return nums


def quick_sort(nums):

    def partition(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    res = []
    for _ in range(size):
        res.append(random.randint(at, to))
    return res


my_list = gen_list(15)
print(*my_list)
print(f'Bubble sort: {bubble_sort(my_list)}')
print(f'Sort choice: {sort_choice(my_list)}')
print(f'Quick sort: {quick_sort(my_list)}')
