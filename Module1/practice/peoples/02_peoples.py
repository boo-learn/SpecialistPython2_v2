from collections import Counter


class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age: int) -> None:
        # TODO: скопируйте реализацию метода из предыдущей задачи
        if type(new_age) == int and 1 < new_age < 100:
            self.age = new_age
        else:
            print('Incorrect age value')

    def full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def full_info(self) -> str:
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
youngest_person = peoples[0]
for people in peoples:
    if people.age < youngest_person.age:
        youngest_person = people
    index +=1
print(youngest_person.name, youngest_person.surname)


# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"

dict_name_surname = {}
age_list = []
unique_values_list = []

for value in range(len(peoples)):
    if not peoples[value].name + ' ' + peoples[value].surname in dict_name_surname:
        dict_name_surname[peoples[value].name + ' ' + peoples[value].surname] = [peoples[value].age, 1]
        continue
    if peoples[value].name + ' ' + peoples[value].surname in dict_name_surname and peoples[value].age == dict_name_surname[peoples[value].name + ' ' + peoples[value].surname][0]:
        dict_name_surname[peoples[value].name + ' ' + peoples[value].surname][1] +=1


for key, value in dict_name_surname.items():
    if value[1] >= 2:         
        continue        
    else:
        age_list.append(value[0])        
        dict_once_met = dict(Counter(age_list))

for key, value in dict_once_met.items():
    if value > 1:
        continue
    else:
        unique_values_list.append(key)  

if len(unique_values_list) == len((dict_name_surname)):
    print("одногодок нет")

for key, value in dict_name_surname.items():
    if value[1] >= 2:
        for i in range(value[1]):
            print(key)            
    elif value[0] not in unique_values_list:
        print(key)




