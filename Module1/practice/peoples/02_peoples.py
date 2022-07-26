class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if type(new_age) == int and 1 <= new_age <= 100:
            self.age = new_age
        else:
            print("Некорректный возраст")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 10),
    People("Алена", "Перова", 11),
    People("Василий", "Быстров", 12),
    People("Ольга", "Подгорная", 11),
    People("Иван", "Иванов", 25),
]

min = peoples[0].age
last_name = str(None)
name = str(None)
for lst in peoples:

    if lst.age <= min:
        min = lst.age
        last_name = lst.surname
        name = lst.name

print("Минимальный возраст у: ", last_name, " ", name, ': ', min)

peoples.sort(key=lambda people: people.age)

flg = int(0)

for index, i in enumerate(peoples):
    if index + 1 <= len(peoples) - 1:
        if (i.age == peoples[index + 1].age) or (i.age == peoples[index - 1].age):
            print(i.full_name(), ': ', i.age)
            flg += 1
    elif index == len(peoples) - 1:
        if i.age == peoples[index - 1].age:
            print(i.full_name(), ': ', i.age)
            flg += 1

if flg == 0:
    print("Одногодок нет")


