class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age: int) -> None:
        if type(new_age) == int and 1 < new_age < 100:
            self.__age = new_age
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
yong = peoples[0]
for people in peoples:
    if people.age < yong.age:
        yong = people
print(yong.full_name())

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"


for people in peoples:
    voz = people.age
    for people2 in peoples:
        if people != people2:
            if voz == people2.age:
                print(people.full_name(), people2.full_name())
