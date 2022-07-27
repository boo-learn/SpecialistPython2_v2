class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        # TODO: скопируйте реализацию метода из предыдущей задачи
        ...

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 55),
    People("Ольга", "Подгорная", 32),
]

# TODO-1: найдите самого молодого человека и выведите его Фамилию и Имя
#  Примечание: Если самых молодых несколько, выведите любого

youngs = min(peoples, key=lambda people: people.age)
print(youngs.full_name(), youngs.age)

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"

odnogodki = []

for people in peoples:
    for n in range(len(peoples)):
        if people.age == peoples[n].age:
            if people.full_name() in odnogodki or people.full_name() == peoples[n].full_name():
                continue
            else:
                odnogodki.append(people.full_name())

print(odnogodki) if odnogodki else print("Одногодков нет")

