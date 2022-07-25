class People:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def change_age(self, new_age):
        # Корректным возрастом считаем целое число от 1 до 100
        # Если задан некорректный возраст, выводим "некорректное значение для возраста" и оставляем старое значение
        # Метод ничего не возвращает в качестве результата, а только меняем свойство self.age на значение new_age
        # TODO: напишите реализацию данного метода
        try:
            if type(new_age) == int and 1 <= new_age <= 100:
                self.__age = new_age
                print("Возраст установлен")
            else:
                raise ValueError(f"Некорректное значение для возраста")
        except ValueError as ex:
            print(ex)

    def get_age(self):
        # TODO: скопируйте реализацию метода из предыдущей задачи
        return self.__age

    def full_name(self):
        return f"{self.surname} {self.name}"

    def full_info(self):
        return f"Человек: {self.surname} {self.name} и ему {self.__age} лет"

    def get_fi(self):
        return f"{self.surname} {self.name}"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 55),
    People("Ольга", "Подгорная", 32),
    People("Василь", "Пупкин", 2),
    People("Игорь", "Николаев", 55),
    People("Ещё", "Один", 55),
]

# TODO-1: найдите самого молодого человека и выведите его Фамилию и Имя
#  Примечание: Если самых молодых несколько, выведите любого
min_age = peoples[0].get_age()
min_fi = peoples[0].get_fi()


for ppl in peoples:
    tmp_age = ppl.get_age()
    if tmp_age < min_age:
        min_age = tmp_age
        min_fi = ppl.get_fi()


print(f"Самым молодым является {min_fi}, ему {min_age}")

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"


counter1 = 0
counter2 = 0
peoples_list_length = len(peoples)

if peoples_list_length > 2:
    # Работаем только со списками от 2 и более человек
    for counter1 in range(0, peoples_list_length):
        for counter2 in range(counter1+1, peoples_list_length):
            if peoples[counter1].get_age() == peoples[counter2].get_age():
                print(f"{peoples[counter1].get_fi()} и {peoples[counter2].get_fi()} одногодки. Им : {str(peoples[counter2].get_age())}!")
else:
    print('Добавьте людей для сравнения!')
