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
print("Список сотрудников отсортированный по уменьшению ЗП:")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

def sort_choice(def_staff):
    i = 0
    while i < len(def_staff) - 1:
        m = i
        j = i + 1
        while j < len(def_staff):
            if def_staff[j]['salary'] < def_staff[m]['salary']:
                m = j
            j += 1
        def_staff[i], def_staff[m] = def_staff[m], def_staff[i]
        i += 1

sort_choice(staff)
salary_sum = 0
for i in range(len(staff)):    
    if i <= 2: 
        salary_sum += staff[i]['salary']
    print(f"{staff[i]['name']} {staff[i]['surname']}")
print(salary_sum)
