class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        # Корректным возрастом считаем целое число от 1 до 100
        # Если задан некорректный возраст, выводим "некорректное значение для возраста" и оставляем старое значение
        # Метод ничего не возвращает в качестве результата, а только меняем свойство self.age на значение new_age
        if new_age in range(1, 100):
            self.age = new_age
        else:
            print(f'Введено некорректное значение возраста: {new_age}')

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Создадим двух человек:
people1 = People("Иван", "Уткин", 27)
people2 = People("Алексей", "Перов", 35)
people3 = People("Василий", "Быстров", 65)

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())

print("Меняем возраст людей")
people1.change_age(45)
people2.change_age("help")
people2.change_age(-30)

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())
