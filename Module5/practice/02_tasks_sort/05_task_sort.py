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


def sort_choice(staff):
    i = 0
    while i < len(staff) - 1:
        m = i
        j = i + 1
        while j < len(staff):
            if staff[j]['salary'] > staff[m]['salary']:
                m = j
            if staff[j]['salary'] == staff[m]['salary']:
                if staff[j]['surname'] < staff[m]['surname']:
                    m = j
            j += 1
        staff[i], staff[m] = staff[m], staff[i]
        i += 1

def main():
    sort_choice(staff)
    for n, st in enumerate(staff, 1):
        print(n, st["surname"], st["name"], st["salary"])

    # 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
    salary = [i['salary'] for i in staff]
    print(sum(salary[:-3]))

if __name__ == '__main__':
    main()
