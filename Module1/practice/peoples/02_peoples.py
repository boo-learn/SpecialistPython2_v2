class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age):
        # TODO: скопируйте реализацию метода из предыдущей задачи
        if type(new_age)==int and (new_age>=1) and (new_age<=100):
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
 #   People("Ольга", "Подгорная", 32),
]

def youngest(peoples):
    youngest_people=peoples[0]
    for people in peoples:
        if people.age<youngest_people.age:
            youngest_people=people
    return youngest_people.full_name()
# TODO-1: найдите самого молодого человека и выведите его Фамилию и Имя
#  Примечание: Если самых молодых несколько, выведите любого
print(youngest(peoples))
# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"
def same_age(peoples):
    same_age_people=[]
    for people1 in peoples:
        count=0
        for people2 in peoples:
            if people2.age==people1.age:
                count+=1
            if count>=2:
                same_age_people.append(people1)
    if len(same_age_people)==0:
        print("одногодок нет")
    return same_age_people

for people in same_age(peoples):
    print(people.full_name())
