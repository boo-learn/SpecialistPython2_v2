# "Друзья друзей"
# У всех людей, по крайне мере я надеюсь, есть друзья. У ваших друзей тоже есть друзья и так далее.
# Вы решили запустить свой бизнес и пригласить максимальное количество людей на его открытие.
# Вам в руки попала, как нельзя кстати, база людей со списком их друзей.
# Считаем, что комбинация Имя+Фамилия нам позволяет однозначно идентифицировать человека.

# Задача
# По предоставленным данным(файл peoples.json) определите:
# 1. Сколько людей придет на открытие, если вы отправляете приглашение конкретному человеку
# (любому, на ваш выбор, из базы), а тот всем друзьям, друзья друзьям и т.д.

# 2. Какому минимальному числу людей, нужно отправить приглашение,
# чтобы пришли ВСЕ люди, присутствующие в базе?


# Сюда отправляем полное решение

class Person:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        self.friends_list = []



class Peoples:

    def __init__(self):
        self.person_list = []
        self.index = -1

    def find_or_create_person(self, name, surname, create_if_not_exists = True):

        for person in self.person_list:
            if person.name == name and person.surname == surname:
                return person

        if  create_if_not_exists==False:
            return None

        self.index += 1
        new_person = Person(self.index, name, surname)
        self.person_list.append(new_person)

        return new_person

    def load_data(self, data):  # Загрузка начальных данных

        self.index = -1
        self.person_list.clear()

        for element in data:
            person = self.find_or_create_person(element['name'], element['surname'])

            for friend in element['friends']:
                friend = self.find_or_create_person(friend['name'], friend['surname'])
                friend.friends_list.append(person.id)
                person.friends_list.append(friend.id)

    def find_person_friends_count(self, name, surname):  # Найти количество друзей

        # строим граф связей
        friends_graph = []
        for person in self.person_list:
            friends_graph.append(person.friends_list)

        person = None
        person = self.find_or_create_person(name, surname,False)

        if person is None:
            raise ValueError("Такой человек не найден")

        friends_marks = self.bfg(person.id , friends_graph)

        frinds_count = sum((1 for m  in friends_marks if m > 0))

        return frinds_count

    def bfg(self,p_start, graph):
        start = p_start
        lengths = [None] * (len(graph))
        lengths[start] = 0
        queue = [start]
        while queue:
            cur_vertex = queue.pop(0)
            for vertex in graph[cur_vertex]:
                if lengths[vertex] is None:
                    lengths[vertex] = lengths[cur_vertex] + 1
                    queue.append(vertex)

        return lengths


data = [
    {
        "name": "Вячеслав",
        "surname": "Сидоров",
        "friends": [
            {
                "name": "Дмитрий",
                "surname": "Гаврилов"
            },
            {
                "name": "Владислав",
                "surname": "Иванов"
            },
            {
                "name": "Иван",
                "surname": "Быстров"
            },
            {
                "name": "Андрей",
                "surname": "Хмельнов"
            },
            {
                "name": "Владислав",
                "surname": "Барин"
            },
            {
                "name": "Андрей",
                "surname": "Быстров"
            },
            {
                "name": "Вячеслав",
                "surname": "Васин"
            }
        ]
    },
    {
        "name": "Вячеслав",
        "surname": "Иванов",
        "friends": [
            {
                "name": "Дмитрий",
                "surname": "Гаврилов"
            },
            {
                "name": "Андрей",
                "surname": "Васин"
            },
            {
                "name": "Иван",
                "surname": "Быстров"
            },
            {
                "name": "Андрей",
                "surname": "Хмельнов"
            },
            {
                "name": "Петр",
                "surname": "Иванов"
            }
        ]
    },
    {
        "name": "Дмитрий",
        "surname": "Гаврилов",
        "friends": [
            {
                "name": "Андрей",
                "surname": "Быстров"
            },
            {
                "name": "Дмитрий",
                "surname": "Быстров"
            },
            {
                "name": "Андрей",
                "surname": "Васин"
            },
            {
                "name": "Владислав",
                "surname": "Иванов"
            },
            {
                "name": "Алексей",
                "surname": "Иванов"
            },
            {
                "name": "Вячеслав",
                "surname": "Барин"
            }
        ]
    },
    {
        "name": "Андрей",
        "surname": "Васин",
        "friends": [
            {
                "name": "Андрей",
                "surname": "Хмельнов"
            },
            {
                "name": "Петр",
                "surname": "Иванов"
            },
            {
                "name": "Алексей",
                "surname": "Сидоров"
            },
            {
                "name": "Вячеслав",
                "surname": "Васин"
            },
            {
                "name": "Алексей",
                "surname": "Иванов"
            }
        ]
    },
    {
        "name": "Владислав",
        "surname": "Иванов",
        "friends": [
            {
                "name": "Вячеслав",
                "surname": "Иванов"
            },
            {
                "name": "Андрей",
                "surname": "Хмельнов"
            },
            {
                "name": "Владислав",
                "surname": "Барин"
            },
            {
                "name": "Петр",
                "surname": "Иванов"
            },
            {
                "name": "Алексей",
                "surname": "Сидоров"
            },
            {
                "name": "Дмитрий",
                "surname": "Быстров"
            },
            {
                "name": "Вячеслав",
                "surname": "Барин"
            },
            {
                "name": "Вячеслав",
                "surname": "Куролесов"
            },
            {
                "name": "Иван",
                "surname": "Хмельнов"
            }
        ]
    },
    {
        "name": "Иван",
        "surname": "Гриб",
        "friends": [
            {
                "name": "Андрей",
                "surname": "Хмельнов"
            },
            {
                "name": "Андрей",
                "surname": "Быстров"
            },
            {
                "name": "Вячеслав",
                "surname": "Куролесов"
            },
            {
                "name": "Иван",
                "surname": "Хмельнов"
            }
        ]
    }
]

people_list = Peoples()
people_list.load_data(data)

person_name = "Дмитрий"
person_surname = "Быстров"

print(f" Если послать приглашение человеку {person_name} {person_surname}, то прийдет {people_list.find_person_friends_count(person_name, person_surname)} чел.")
