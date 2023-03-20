class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.__age = age

    def change_age(self, new_age: int) -> None:
        # Корректным возрастом считаем целое число от 1 до 100
        # Если задан некорректный возраст, выводим "некорректное значение для возраста" и оставляем старое значение
        # Метод меняет свойство self.age на значение new_age
        # TODO: напишите реализацию данного метода
        if type(new_age) == int and 1 < new_age < 100:
            self.__age = new_age
        else:
            print("Некорректное значение для возраста")

    def full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def full_info(self) -> str:
        return f"Человек: {self.surname} {self.name} и ему {self.__age} лет"


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
# добавил еще 2 кейса
people2.change_age(1)
people2.change_age(5.5)

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())
