def bubble_sort(_staff):
    print(f'Run')
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(_staff) - 1 - j):
            if (_staff[i]["salary"] > _staff[i + 1]["salary"]) or (_staff[i]["salary"] == _staff[i + 1]["salary"] and _staff[i]["surname"] + _staff[i]["name"] > _staff[i + 1]["surname"] + _staff[i + 1]["name"]):
                _staff[i], _staff[i + 1] = _staff[i + 1], _staff[i]
                swapped = True
        j += 1

def print_staff(_staff):
    for i in _staff:
        print(f', salary = {i["salary"]}, {i["surname"]} {i["name"]}')

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
    },
]

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии

print_staff(staff)

bubble_sort(staff)
print("Список сотрудников отсортированный по уменьшению ЗП:")
print_staff(staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
print("Найдите сумму зарплат трех самых низкооплачиваемых сотрудников")
summa = 0
for s in staff[:3:]:
    summa += s["salary"]
# summa = sum(staff[-3::]["salary"])
print(summa)

#   print(sum(staff[:3]["salary"])) ?????????????????????????????????????
