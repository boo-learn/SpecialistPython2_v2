class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age: int) -> None:
        # TODO: скопируйте реализацию метода из предыдущей задачи
        ...

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

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"
ages = []
same_age = 0
same_age_peoples = []
for person in peoples:
    ages.append(person.age)
for age in ages:
    if ages.count(age) != 1:
        same_age = age
for person in peoples:
    if person.age == same_age:
        same_age_peoples.append(person.full_name())
if same_age_peoples == []:
    print('Одногодок нет')
else:
    print(same_age_peoples)
