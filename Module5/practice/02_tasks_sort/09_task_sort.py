employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"}
]

sorted(employees, key=lambda emp: (emp['surname'], emp['name']))
print(employees)

for emp in employees:
    print(f"{emp['surname']} {emp['name']}")
