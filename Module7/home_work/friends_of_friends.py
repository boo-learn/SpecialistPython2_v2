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
import json

f = open('peoples.json', 'r', encoding='utf-8')
peoples_json = json.load(f)
f.close()


class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.friends = []

    def __str__(self):
        friends = []
        for friend in self.friends:
            friends.append(f"{friend.surname} {friend.name}")
        return f"{self.surname} {self.name} friends:[{', '.join(friends)}]"


def get_people(peoples, name, surname):
    result = list(filter(lambda x: (name, surname) == (x.name, x.surname), peoples))
    return None if len(result) == 0 else result[0]


def get_id(peoples, name, surname):
    i = 0
    for people in peoples:
        if f"{people.surname} {people.name}" == f"{surname} {name}":
            return i
        i += 1
    return None


def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)

    return visited


peoples = []
friends = []
for people in peoples_json:
    people_in_base = get_people(peoples, people['name'], people['surname'])
    if people_in_base is None:
        people_in_base = People(people['name'], people['surname'])
        peoples.append(people_in_base)
    friends.append(people_in_base)
    for friend in people['friends']:
        friend_in_base = get_people(peoples, friend['name'], friend['surname'])
        if friend_in_base is None:
            friend_in_base = People(friend['name'], friend['surname'])
            peoples.append(friend_in_base)
        # friend_in_base.friends.append(people_in_base) #если добавить обратную связь, то получится полносвязный граф.
        people_in_base.friends.append(friend_in_base)

graph = []
id_friends_in_peoples = []
for friend in friends:
    id_friends_in_peoples.append(get_id(peoples, friend.name, friend.surname))
for people in peoples:
    edges = []
    for friend in people.friends:
        edges.append(get_id(peoples, friend.name, friend.surname))
    graph.append(edges)
for start in id_friends_in_peoples:
    visited = dfs(graph, start)
    print(f"Если отправить приглашение {peoples[start]}, то придет {sum(visited)} человек")

# Ответ на вопрос 2:
# Достаточно послать двум
# Если отправить приглашение Сидоров Вячеслав friends:[Гаврилов Дмитрий ,Иванов Владислав ,Быстров Иван ,Хмельнов Андрей ,Барин Владислав ,Быстров Андрей ,Васин Вячеслав], то придет 17 человек
# Если отправить приглашение Гриб Иван friends:[Хмельнов Андрей ,Быстров Андрей ,Куролесов Вячеслав ,Хмельнов Иван], то придет 5 человек
# Но это я определил по visited, алгоритм не придумал, ушел спать :)
