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

from pprint import pprint


def bubble_sort(nums, key=lambda x: x, reverse=False):
   swapped = True
   j = 0
   while swapped:
      swapped = False
      for i in range(len(nums) - 1 - j):
         if reverse:
            expr = key(nums[i]) < key(nums[i + 1])
         else:
            expr = key(nums[i]) > key(nums[i + 1])
         if expr:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True
      j += 1
   return nums


if __name__ == '__main__':
   pprint(bubble_sort(employees, key=(lambda x: (x['position'], x['surname'], x['name']))))
