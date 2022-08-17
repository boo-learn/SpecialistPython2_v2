from pprint import pprint
def choice_sort(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            fullname1 = nums[j]['name'] + nums[j]['surname']
            fullname2 = nums[m]['name']+ nums[m]['surname']
            if nums[j]['salary'] > nums[m]['salary'] or nums[j]['salary'] == nums[m]['salary'] and fullname1 < fullname2:
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
    },
]

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии

print("Список сотрудников отсортированный по уменьшению ЗП:")
choice_sort(staff)
pprint(staff)


# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

summary = staff[-1]['salary'] + staff[-2]['salary'] + staff[-3]['salary']
print(summary)
