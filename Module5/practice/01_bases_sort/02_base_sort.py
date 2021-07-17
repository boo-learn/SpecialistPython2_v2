# Все алгоритмы сортировки из examples/ оберните в функции
# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at = -100, to = 100):
    import random
    lst = []
    for _ in range(size):
        lst.append(random.randint(at, to))
    return lst
nums = gen_list(100)

count = 0


def bubble_sort(nums):
    swapped = True
    j = 0
    count = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                count += 1
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j +=1
        return nums
    #print("after sort = ", nums)
        
    #print("count = ", count)


def sort_choice():
    i = 0
    count = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            count += 1
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
#     print("after sort = ", nums)
#     print("count = ", count)
        return nums




def quick_sort():

    count = 0
    def partition(nums, low, high):
        global count
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            count  += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]


    def quick_sort(nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # Индекс опорного элемента
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)


# Проверяем, что оно работает
gen_list(100)
print("before sort = ", nums)
#quick_sort(nums)
bubble_sort(nums)
print("after sort = ", nums)

#print("count = ", count)

