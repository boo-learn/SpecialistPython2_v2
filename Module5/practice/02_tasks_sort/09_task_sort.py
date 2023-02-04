

def sort_choice(nums: list) -> None:
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


employees = [
    {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
    {"name": "Иван", "surname": "Петров", "position": "Прораб"},
    {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
    {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]

surname_list = []
for emp in employees:
    surname_list.append(emp["surname"])

sort_choice(surname_list)  # сортируем список фамили

# # сортируем словарь employees по фамилиям
for i, sal in enumerate(surname_list):
    for j, emp in enumerate(employees):
        if emp["surname"] == sal and i != j:
            employees[i], employees[j] = employees[j], employees[i]


name_list = []  # создаем список с именами отсортированный по фамилиям
for emp in employees:
    name_list.append(emp["name"])


surname_dict = {}  # создаем словарь где ключи это фамилия а значения это список имен сотрудников с такой фамилией

for i, sal in enumerate(surname_list):
    if not surname_dict.get(sal):
        surname_dict[sal] = []
    surname_dict[sal].append(name_list[i])

for item in surname_dict.values():  # сортируем списки значений словаря
    sort_choice(item)

res_list = []  # итоговый список
for value in surname_dict.values():  # наполняем список по порядку значений в словаре с ключами зп
    for i in value:
        for emp in employees:
            if emp['name'] == i:
                if f"{emp['surname']} {emp['name']}" not in res_list:
                    res_list.append(f"{emp['surname']} {emp['name']}")
# решение аналагично решению в задании 5
print(res_list)
