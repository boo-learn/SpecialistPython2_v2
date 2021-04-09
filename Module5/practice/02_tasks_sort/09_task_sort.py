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


def my_sort_func(my_dict):
    return my_dict.get("surname") + my_dict.get("name")


bubble_sort(employees, key=my_sort_func)
for i in range(len(employees)):
    print(f'{employees[i]["surname"]} {employees[i]["name"]}')
