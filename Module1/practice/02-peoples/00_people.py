class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name_v1(self) -> str:
        return f"{self.surname} {self.name}"

    def full_name_v2(self) -> None:
        print(f"{self.surname} {self.name}")


# Создадим двух человек:
people1 = People("Иван", "Уткин", 27)
people2 = People("Алексей", "Перов", 35)

# Выведем данные о человеке, используя оба варианта методов:

...

# Какой метод предпочтительнее?
