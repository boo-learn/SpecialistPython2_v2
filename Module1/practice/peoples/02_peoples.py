class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if type(new_age) == int and new_age >= 1 and new_age <= 100:
            age = new_age

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

min_person = peoples[0]

for person in peoples:
    if min_person.age > person.age:
        min_person = person

print("Самый молодой человек ", min_person.full_info())

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"


new_list = set()
for person in peoples:
    for person2 in peoples:
        if person.age == person2.age and person != person2:
                new_list.add(person)
                new_list.add(person2)

if len(new_list) > 1:
    for new_person in new_list:
        print(new_person.full_info())
else:
    print("одногодок нет")

