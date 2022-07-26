class People:
    def __init__(self, name, surname, age: float):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return f"{self.surname} {self.name}"


# Создадим двух человек:
people1 = People("Иван", "Уткин", 27)
people2 = People("Алексей", "Перов", 35)

# Определим кто старше:
if people1.age < people2.age:
    print(f"{people1.full_name()} младше {people2.full_name()}")
elif people1.age > people2.age:
    print(f"{people2.full_name()} младше {people1.full_name()}")
else:
    print(f"{people1.full_name()} и {people2.full_name()} одногодки")

print("Меняем возраст")
people1.age = 45  # Меняем возраст первого человека
people2.age = "hello"  # Меняем возраст второго, на некорректное значение

# Снова пытаемся определить кто старше:
try:
    if people1.age < people2.age:  # И падаем с ошибкой...
        print(f"{people1.full_name()} младше {people2.full_name()}")
    elif people1.age > people2.age:
        print(f"{people2.full_name()} младше {people1.full_name()}")
    else:
        print(f"{people1.full_name()} и {people2.full_name()} одногодки")
except TypeError:
    print("Некорректное значение возраста")

# Как защититься от установки некорректных свойств?
