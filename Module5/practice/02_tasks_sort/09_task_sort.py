# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:

def sort_choice_s(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j]['surname'] > nums[m]['surname']:
                m = j
            elif nums[j]['surname'] == nums[m]['surname'] and nums[j]['name'] > nums[m]['name']:
                m = j

            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


employees = [
    {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
    {"name": "Иван", "surname": "Петров", "position": "Прораб"},
    {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
    {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.
sort_choice_s(employees)
employees.reverse()
for person in employees:
    print(
        f" Фамилия: {person['surname']}, Имя: {person['name']}")
