class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        # TODO: скопируйте реализацию метода из предыдущей задачи
        if type(new_age) == int and new_age >= 1 and new_age <= 100:
            self.age = new_age
        else:
            print("некорректное значение для возраста")

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
zero_people1 = peoples[0]
for i in peoples:
    if zero_people1.age > i.age:
        zero_people1 = i
print (zero_people1.full_name())
# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"

p=[]
for i in peoples:
    for j in peoples:
        if i.age == j.age and i.full_name() != j.full_name():
            p.append(i.full_name())
if len(p)>0:
    for y in p:
        print(y)
else:
    print ("одногодок нет")
