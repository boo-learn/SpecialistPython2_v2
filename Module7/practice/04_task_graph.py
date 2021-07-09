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
import random

class People:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __eq__(self, other):
        if self.name == other.name and self.surname == other.surname:
            return True
        return False

    def __repr__(self):
        return f"{self.number} {self.surname} {self.name}"


# def get_friends(lst, el):
#     for val in lst:
#         if eq(val, el):
#             return el['friends']
#     return []
#
#
# def eq(ppl1, ppl2):
#     if ppl1['name'] == ppl2['name'] and ppl1['surname'] == ppl2['surname']:
#         return True
#     return False
#
#
# def add_friends():
#     pass

def create_graph():
    # random_people = all_peoples[random.randrange(len(all_peoples))]
    # ppl = People(random_people['name'], random_people['surname'])
    # unique_people = [ppl]
    # add_friends(random_people['friends'])
    unique_people = []
    graph = []
    for people in all_peoples:
        ppl = People(people['name'], people['surname'], len(unique_people))
        if ppl not in unique_people:
            unique_people.append(ppl)
            graph.append([])
        for fr in people['friends']:
            ppl_fr = People(fr['name'], fr['surname'], len(unique_people))
            if ppl_fr not in unique_people:
                unique_people.append(ppl_fr)
                graph.append([])
            graph[unique_people.index(ppl)].append(unique_people.index(ppl_fr))
    return unique_people, graph


def bfs(graph, start):
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


def dfs(graph, start):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start)
    return visited


with open("peoples.json", "r", encoding="utf-8") as file:
    all_peoples = json.load(file)
    unique_people, graph = create_graph()
    print(unique_people)
    print(graph)

    print("1. Сколько людей придет на открытие, если вы отправляете приглашение конкретному человеку")
    random_people = random.randrange(len(unique_people))
    res = dfs(graph, random_people)
    print(res)
    print(f"отправили {random_people} - придет {sum(res)}")

    print(f"Какому минимальному числу людей, нужно отправить приглашение, # чтобы пришли ВСЕ люди, присутствующие в "
          f"базе?")
    res = []
    max_res = -1
    for i in range(len(unique_people)):
        res.append(dfs(graph, i))
    res.sort(key=lambda x: sum(x), reverse=True)

## FIXME
    cnt = 1
    summary = res[0]
    for i in range(len(unique_people)-1):
        summary += res[i]
        if sum(summary) == len(unique_people):
            print(cnt)
            break
        cnt += 1
    print("Нельзя пригласить всех")

    # print("")
    # for i in range(len(unique_people)):
    #     print(sum(res[i]), end="")
