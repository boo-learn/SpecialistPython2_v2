def sort_choice(lst, reverse=False, key=lambda n: n):
    i = 0
    while i < len(lst) - 1:
        m = i
        j = i + 1
        while j < len(lst):
            if reverse:
                condition = key(lst[j]) > key(lst[m])
            else:
                condition = key(lst[j]) < key(lst[m])

            if condition:
                m = j
            j += 1
        lst[i], lst[m] = lst[m], lst[i]
        i += 1


employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]

sort_choice(employees, key=lambda employee: (employee["surname"], employee["name"]))
num = 1
for name_surname in employees:
    print(f"{num}. {name_surname['surname']} {name_surname['name']}")
    num += 1
