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
            print("Некорректный возраст")

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
the_youngest = peoples[0]
for person in peoples:
    if person.age < the_youngest.age:
        the_youngest = person
print(f'Самый молодой человек - это {the_youngest.full_name()}')

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"
same_age_peoples = []
for i in range(len(peoples)):
    current_age = peoples[i].age
    for j in range(i+1, len(peoples)):
        if peoples[j].age == current_age:
            same_age_peoples.append(peoples[i])
            same_age_peoples.append(peoples[j])

if len(same_age_peoples) > 0:
    for person in same_age_peoples:
        print(person.full_name())
else:
    print('Одногодок нет')
