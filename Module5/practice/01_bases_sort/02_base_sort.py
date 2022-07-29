# Все алгоритмы сортировки из examples/ оберните в функции

def bubble_sort():


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


nums = [5, 2, -1, 8, 4, -4, 7]
print("before sort = ", nums)
bubble_sort(nums)
print("after sort = ", nums)

def quick_sort():
    pass


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    pass

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
