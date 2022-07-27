# Дан список сотрудников:

def bubble_sort(staff):
    swapped = True
    k = 1
    while swapped:
        swapped = False
        for i in range(len(staff) - 1):
            if staff[i]['salary'] > staff[i + 1]['salary']:
                staff[i], staff[i + 1] = staff[i + 1], staff[i]
                swapped = True
            elif staff[i]['salary'] == staff[i + 1]['salary']:
                if staff[i]['name'] > staff[i + 1]['name']:
                    staff[i], staff[i + 1] = staff[i + 1], staff[i]

        k += 1
    return staff


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
# res = []
# for i in staff:
#     res.append(i['salary'])
#
# res.sort(reverse=True)
# print(res)
#
# for j in range(len(res)):
#     for i in staff:
#         if i['salary'] == res[j]:
#             print(i['surname'], i['name'])
#     j += 1

# print(type(staff))
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
print("Список сотрудников отсортированный по уменьшению ЗП:", bubble_sort(staff)[::-1])

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

