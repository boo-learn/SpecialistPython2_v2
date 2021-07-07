# Все алгоритмы сортировки из examples/ оберните в функции

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return (nums)


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
    return(nums)


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

    def quick_sort(nums):
        def _quick_sort(items, low, high):
            if low < high:
                # Индекс опорного элемента
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)
    return(nums)




# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    list1 = []
    for _ in range(size):
        k = random.randint(at,to)
        list1.append(k)
    return list1
k = gen_list(10)
print(k)
print('bubble sort:', bubble_sort(k))
print('sort_choice:', sort_choice(k))
print(' quick_sort:', quick_sort(k))


# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
