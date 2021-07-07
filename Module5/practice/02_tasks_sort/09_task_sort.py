# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.


def employee_format(employee: {}) -> str:
   return str(employee["surname"]) + str(employee["name"])


def sort_choice(nums: [], rule: lambda n: n) -> []:
   i = 0
   while i < len(nums) - 1:
      m = i
      j = i + 1
      while j < len(nums):
         if rule(nums[j]) < rule(nums[m]):
            m = j
         j += 1
      nums[i], nums[m] = nums[m], nums[i]
      i += 1
   return nums


print(employees)
# print(employee_format(employees[0]))
sort_choice(employees, rule=employee_format)
for emp in employees:
   print(emp["surname"] + ' ' + emp["name"])
