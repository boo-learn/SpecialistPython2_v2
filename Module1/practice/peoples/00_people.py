class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self) -> str:
        return f"{self.surname} {self.name}"


# Создадим двух человек:
people1 = People("Иван", "Уткин", 27)
people2 = People("Алексей", "Перов", 35)

print("Меняем возраст")
people1.age = 45  # Меняем возраст первого человека
people2.age = "hello"  # Меняем возраст второго, на некорректное значение

# Определим кто старше:
if people1.age < people2.age:
    print(f"{people1.full_name()} младше {people2.full_name()}")
elif people1.age > people2.age:
    print(f"{people2.full_name()} младше {people1.full_name()}")
else:
    print(f"{people1.full_name()} и {people2.full_name()} одногодки")
