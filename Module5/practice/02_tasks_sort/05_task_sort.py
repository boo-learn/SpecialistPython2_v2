# Дан список сотрудников:
staff = [
    {
        'name': 'Григорий',
        'surname': 'Зуев',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Абвов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Иванов',
        'salary': 34500
    },
]

def sort_choice(staff):
    i = 0
    while i < len(staff) - 1:
        m = i
        j = i + 1
        while j < len(staff):
            if staff[j]['salary'] > staff[m]['salary']: #Скрипт сортировки скорректиров в части зарплат
                m = j
            elif staff[j]['salary'] == staff[m]['salary']: #Скрипт сортировки скорректиров в части фамилий
                if staff[j]['surname'][0] < staff[m]['surname'][0]: #Скрипт сортировки скорректиров в части фамилий
                    m = j
            j += 1
        staff[i], staff[m] = staff[m], staff[i]
        i += 1
#print(staff)
sort_choice(staff)
#print(staff)
# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии

persons = []
for person in staff:
    persons.append(person['surname'])

print("Список сотрудников отсортированный по уменьшению ЗП:")
print(*persons, sep=', ')

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
sumv = 0
staff.reverse()

number_of_persons = 0
for person in staff:
    sumv += person['salary']
    number_of_persons += 1
    if number_of_persons == 3:
        break

print(sumv)
