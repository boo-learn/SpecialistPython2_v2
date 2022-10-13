

employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
   {"name": "Аленина", "surname": "Алагуз", "position": "Повар"}
]

employees.sort(key = lambda employ: (employ['surname'], employ['name']))
print(employees)
for employ in employees:
    print(employ['surname'], employ['name'])
