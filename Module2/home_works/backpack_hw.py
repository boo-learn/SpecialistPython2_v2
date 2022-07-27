class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if type(new_age) == int and 1 < new_age < 100:
            self.age = new_age
        else:
            print("Некорректное значение для возраста")

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"
       
# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 2),
    People("Алена", "Перова", 12),
    People("Василий", "Быстров", 22),
    People("Ольга", "Подгорная", 44),
    People("Сашка", "Пупкин", 88),
    People("Машка", "Дудкина", 32),
]

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"

counter_2 = 0
len_peoples = range(0, len(peoples))
for i in len_peoples:
    counter = 0
    shot_peoples = peoples.copy()
    double_people = shot_peoples.pop(i)
    for people in shot_peoples:
        if double_people.age == people.age:
            counter += 1
            if counter == 1:            #  Почему не срабатывает просто if counter:  ??
                print(double_people.full_name())
                counter_2 += 1
# print(counter_2)
if not counter_2:
    print("одногодок нет")
