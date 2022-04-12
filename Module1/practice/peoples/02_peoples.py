class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        if type(new_age) == int and 1<= new_age<=100:
            self.age=new_age
        else:
            print("некорректное значение для возраста")
        # # TODO: скопируйте реализацию метода из предыдущей задачи
        # ...

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
young_age=peoples[0].age
young_man=peoples[0]

for people in peoples:
    current_age=people.age
    if current_age<young_age:
        young_age=people.age
        young_man=people

print(f"самый молодой человек - {young_man.name} {young_man.surname} и ему {young_man.age}")
# # TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
# #  Примечание: Если одногодок нет, в
