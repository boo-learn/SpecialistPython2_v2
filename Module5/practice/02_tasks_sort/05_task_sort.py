# Дан список сотрудников:

def sort_choice_salary(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j]['salary'] > nums[m]['salary']:
                m = j
            elif nums[j]['salary'] == nums[m]['salary'] and nums[j]['surname'] < nums[m]['surname']:
                m = j

            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


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

sort_choice_salary(staff)

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
print("Список сотрудников отсортированный по уменьшению ЗП:")
print(staff)
for person in staff:
    print(
        f"Имя: {person['name']}, Фамилия: {person['surname']}, ЗП: {person['salary']}")


# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
sum_sal = 0
for sal in staff[-3:]:
    sum_sal += sal['salary']
print(sum_sal)
