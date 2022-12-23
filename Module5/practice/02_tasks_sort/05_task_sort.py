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

def sort_staf(staf_list):
    swapped = True
    cnt = 1
    while swapped:
        swapped = False
        for i in range(len(staf_list) - cnt):
            if staf_list[i]['salary'] <= staf_list[i + 1]['salary']:
                if staf_list[i]['salary'] == staf_list[i + 1]['salary']:
                    if staf_list[i]['surname'] == staf_list[i + 1]['surname']:
                        if staf_list[i]['name'] > staf_list[i + 1]['name']:
                            staf_list[i], staf_list[i + 1] = staf_list[i + 1], staf_list[i]
                    elif staf_list[i]['surname'] > staf_list[i + 1]['surname']:
                        staf_list[i], staf_list[i + 1] = staf_list[i + 1], staf_list[i]
                else:
                    staf_list[i], staf_list[i + 1] = staf_list[i + 1], staf_list[i]
                swapped = True
        cnt += 1


print("Исходный список сотрудников:")
print(staff)
sort_staf(staff)
print("Список сотрудников отсортированный по уменьшению ЗП:")
print(staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
summa = sum(item['salary'] for item in staff[-3:])
print(summa)
