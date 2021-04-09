# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = len(nums) - 1
    while swapped:
        swapped = False
        for i in range(j):
            if reverse:
                condition = key(nums[i]) < key(nums[i + 1])
            else:
                condition = key(nums[i]) > key(nums[i + 1])
            if condition:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j -= 1


def string_sort(my_str):
    l = []
    for char in my_str:
        l.append(char)
    bubble_sort(l)
    return ''.join(l)


my_list = ['воз', 'ключ', 'адрес', 'рука', 'среда', 'зов']
print(my_list)
bubble_sort(my_list, key=string_sort)
for i in range(len(my_list) - 1):
    if string_sort(my_list[i]) == string_sort(my_list[i + 1]):
        print(my_list[i], my_list[i + 1])
