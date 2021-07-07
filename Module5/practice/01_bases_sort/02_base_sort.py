# Все алгоритмы сортировки из examples/ оберните в функции
from random import randint
import random


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
    return nums


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

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

        _quick_sort(nums, 0, len(nums) - 1)
    return nums


# Напишите функцию для заполнения списка случайными числами
def gen_list(size):
    from random import randint
    lst = [randint(-100, 100) for i in range(size)]
    return lst

nums = gen_list(100)
print("nums = ", nums)
nums = bubble_sort(nums)
print("nums_after_bubble = ", nums)
nums = quick_sort(nums)
print("nums_after_quick = ", nums)
nums = sort_choice(nums)
print("nums_sort_choice = ", nums)
