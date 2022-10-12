def sort_choice(nums, key=lambda *args: args , revers=False, mod=lambda n:n): # True/False
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if revers:
                condition = mod(nums[j][key]) > mod(nums[m][key])
            else:
                condition = mod(nums[j][key]) < mod(nums[m][key])
            if condition:
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



# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
print("Список сотрудников отсортированный по уменьшению ЗП:")
sort_choice(staff, 'salary','surname' )
print(staff)
salary_sum =0
for i in range(3):
    salary_sum += staff[i]['salary']
    
print(salary_sum)
