class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def change_age(self, new_age):
        if type(new_age) == int and 0 < new_age < 101:
            self.__age = new_age
        else:
            print("некорректное значение для возраста")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
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

print(people1.full_info())
print(people2.full_info())
print(people3.full_info())
