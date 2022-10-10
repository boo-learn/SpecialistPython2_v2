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
            print("некорректное значение для возраста")

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
ages = [people.age for people in peoples]
for people in peoples:
    if people.age == min(ages):
        print(people.surname, people.name)

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"
answer = []
ages.sort()
for i in range(len(ages)-1):
    if ages[i] == ages[i+1]:
        answer.append(ages[i])
if len(answer) == 0:
    print('одногодок нет')
else:
    for people in peoples:
        if people.age in answer:
            print(people.surname, people.name)
