def bubble_sort(nums: list):
    swapped = True
    j = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1


def sort_choice(nums: list):
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


def quick_sort(nums: list):

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

    def quick_sort(nums):

        def _quick_sort(items, low, high):
            if low < high:
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

    quick_sort(nums)


def gen_list(size: int, at: int, to: int) -> list:
    import random
    return [random.randint(at, to)for i in range(size)]


# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков

list1 = gen_list(10, -100, 100)
list2 = gen_list(10, -100, 100)
list3 = gen_list(10, -100, 100)
print("BEFORE:")
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

quick_sort(list1)
sort_choice(list2)
bubble_sort(list3)
print("AFTER:")
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
