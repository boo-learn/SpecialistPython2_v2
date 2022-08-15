class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if type(new_age) == int and 0 < new_age < 101:
            self.age = new_age
        else:
            print("Некорректное значения для возраста")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 55),
    People("Ольга", "Подгорная", 32),
]

min_age = 101
for man in peoples:
    if man.age < min_age:
        youngest = man

print("Самый молодой -", man.full_name())

flag = 0
for i in range(len(peoples) - 1):
    for j in range(i+1, len(peoples)):
        if peoples[i].age == peoples[j].age:
            print("Одногодки:", peoples[i].full_name(), "и", peoples[j].full_name())
            flag = 1
if not flag:
    print("Одногодок нет")
