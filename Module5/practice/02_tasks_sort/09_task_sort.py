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

def sort_choice(nums, key=lambda el: el, reverse=False):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            comp = key(nums[j]) > key(nums[m]) if reverse else key(nums[j]) < key(nums[m])
            if comp:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

sort_choice(employees, key=lambda x: (x['surname'], x['name']))
for i in employees:
    print(i['surname'], i['name'])
