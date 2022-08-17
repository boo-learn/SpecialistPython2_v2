def sort_choice_staff(nums, rvrs = False, abs_ = False):
    from random import randint

    # Алгоритм:
    # 1. Найти наименьшее значение в списке.
    # 2. Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
    # 3. Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
    # 4. Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
    # 5. Продолжать выполнять поиск и обмен, пока не будет достигнут конец списка.

    # nums = [5, 2, -1, 8, 4, -4, 7]
    print("sort_choice, before sort = ", nums)
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            # a = nums[j].['salary']
            # b = nums[m].['salary']
            a = nums[j]
            b = nums[m]
            a = a['salary']
            b = b['salary']
            if abs_:
                a = abs(a)
                b = abs(b)
            condition = a < b
            if rvrs:
                condition = condition = a > b
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    print("sort_choice, after sort = ", nums)

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
sort_choice_staff(staff)

print(f"Список сотрудников отсортированный по уменьшению ЗП: {staff}")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
sum_ = 0
for item in staff[:3]:
    sum_ += item['salary']
print(sum_)
