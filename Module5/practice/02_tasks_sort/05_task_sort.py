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


# Дан список сотрудников:
staff = [
    {
        'name': 'Григорий',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 34500
    }
]
# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
salary_list = [] 
for emp in staff: # список всех зарплат
    salary_list.append(emp["salary"])

sort_choice(salary_list) # сортируем список зарплат
salary_list = salary_list[-1::-1] # реверсим его (если закоментить эту строчку то будет сортировка по увелечению зп)

# сортируем словарь staff по уменьшению зарплат
for i, sal in enumerate(salary_list): 
    for j, emp in enumerate(staff):
        if emp["salary"] == sal and i != j:
            staff[i], staff[j] = staff[j], staff[i]


emp_list = [] # создаем список с фамилиями по уменьшению зп
for emp in staff:
    emp_list.append(emp["surname"])


sal_dict = {} # создаем словарь где ключи это значение зп а значения это список фамилий сотрудников с такой зп

for i, sal in enumerate(salary_list):
    if not sal_dict.get(sal):
        sal_dict[sal] = []
    sal_dict[sal].append(emp_list[i])


for item in sal_dict.values(): # сортируем списки значений словаря 
    sort_choice(item)


print("Список сотрудников отсортированный по уменьшению ЗП:")
res_list = [] # итоговый список 
for value in sal_dict.values(): # наполняем список по порядку значений в словаре с ключами зп
    for i in value:
        for emp in staff:
            if emp['surname'] == i:
                if f"{emp['surname']} {emp['name']}" not in res_list:
                    res_list.append(f"{emp['surname']} {emp['name']}")
print(res_list)

# # 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

sum_sal = sum(salary_list[-1:1:-1]) # использовал список зарплат
print(f"Сумма зарплат трех самых низкооплачиваемых сотрудников: {sum_sal}")
