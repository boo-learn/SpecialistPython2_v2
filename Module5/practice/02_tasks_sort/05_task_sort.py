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
staff.sort(key=lambda emp: (emp['salary'], emp['surname'], emp['name']))


print("Список сотрудников отсортированный по уменьшению ЗП:")
salary_rank = 1
for emp in staff:
    print(f"{salary_rank}. {emp['name']} {emp['surname']} {emp['salary']}")
    salary_rank += 1


sum_down = sum([emp["salary"] for emp in staff[:3]])
print("Сумма зарплат трех самых низкооплачиваемых сотрудников:", sum_down)
