class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def change_age(self, new_age):
        if type(new_age) == int and 1 <= new_age <= 100:
            self.__age = new_age
        else:
            print("некорректное значение для возраста")

    def get_age(self):
        return (self.__age)

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.__age} лет"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 27),
    People("Василий", "Быстров", 27),
    People("Джон", "Уик", 60),
    People("Ольга", "Подгорная", 32),
]
# TODO-1: найдите самого молодого человека и выведите его Фамилию и Имя
#  Примечание: Если самых молодых несколько, выведите любого
min_age_person = peoples[0].full_name()
min_age = peoples[0].get_age()
for person in peoples:
    my_age = person.get_age()
    if my_age <= min_age:
        min_age = my_age
        min_age_person = person.full_name()
print(f' Самый молодой : {min_age_person}')

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"

same_year = []
cnt = 0
for i in range(len(peoples) - 1):
    for j in range(len(peoples) - 1):
        if peoples[i].get_age() == peoples[j].get_age() and peoples[i] != peoples[j]:
            if peoples[i].full_name() not in same_year:
                same_year.append(peoples[i].full_name())
                cnt += 1
            # same_year.append(peoples[j].full_name())

if cnt == 0:
    print("одногодок нет")
else:
    print("\n******\nОдногодки:")
    for same_pers in same_year:
        print(same_pers)
    print("******")
