class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if type(new_age) == int or 1 < new_age < 100:
            self.age = new_age
        else:
            print(f"Age of {self.surname} is not correct")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 28),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 33),
    People("Ольга", "Подгорная", 33),
    People("Ольга", "Иванова", 28),
]

age_list = []

for person in peoples:
    age_list.append(person.age)

new_age_list = []
i = 0

while i < len(age_list):
    new_age_list.append(age_list.count(age_list[i]))
    i += 1

new_people_list = []

i = 0

while i < len(new_age_list):
    if new_age_list[i] > 1:
        new_people_list.append(peoples[i].full_name())
    i += 1

if len(new_people_list) > 1:
    print(f"Одногодки: {new_people_list}")
else:
    print("Одногодок нет")
