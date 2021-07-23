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
count_el=len(staff)
sort_name_staff=[]
sort_salary_staff=[]
for el in range(count_el):
    min_name=min(staff, key=lambda el:el['name'])
    sort_name_staff.append(min_name)
    staff.remove(min_name)

for el in range(count_el):
    max_salary=max(sort_name_staff, key=lambda el:el['salary'])
    sort_salary_staff.append(max_salary)
    sort_name_staff.remove(max_salary)

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
#print("Список сотрудников отсортированный по уменьшению ЗП:",sort_salary_staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
sum_el=0
i=1
for el in sort_salary_staff[::-1]:
    if i<=3:
        #print(el['salary'])
        sum_el+=el['salary']
        i+=1
print(sum_el)
