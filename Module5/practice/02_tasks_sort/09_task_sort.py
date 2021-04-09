# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employees = [
    {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
    {"name": "Иван", "surname": "Петров", "position": "Прораб"},
    {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
    {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]


# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.

def bubble_sort(nums, key=lambda x: x, reverse=False):
    count = 0
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                count += 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    # print(f'{count=}')

tmp = []
for employee in employees:
    tmp.append(employee['surname'] + ' ' + employee['name'])
bubble_sort(tmp)
print(*tmp, sep='\n')
