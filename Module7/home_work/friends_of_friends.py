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
from copy import deepcopy


def bfs(graph, start_point):
    """Алгоритм изменен для работы со словарями, теперь и на входе и на выходе словарь.
    Логика не изменена: если на выходе дистанция до вершины None, значит пути нет."""
    lengths = {k: None for k in graph.keys()}
    lengths[start_point] = 0
    queue = [start_point]
    while queue:
        cur_vertex = queue.pop(0)
        # if cur_vertex not in graph:
            # continue
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths


def dfs(graph, start_point):
    """Алгоритм изменен для работы со словарями, теперь и на входе и на выходе словарь.
        Логика изменена: теперь на выходе None, если вершина не посещена (сделано для одинаковой фильтрации с bfs)"""
    visited = {k: None for k in graph.keys()}

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_point)
    return visited


# подготовка данных:
# загружаем содержимое json-файла
with open('peoples.json', encoding='utf-8') as jsonfile:
    peoples = json.load(jsonfile)

# упрощаем (как мне кажется) структуру - делаем словарь списков из списка словарей, содержащих списки словарей
peoples_simple = dict()
for people in peoples:
    full_name = f"{people['name']} {people['surname']}"
    friends = [f"{friend['name']} {friend['surname']}" for friend in people['friends']]
    peoples_simple[full_name] = friends
# print(*peoples_simple.items(), sep='\n')

# теперь делаем граф, и связи двусторонними, т.е. если кто-то у кого-то в друзьях, то и у него должны быть друзья
# (можно наверное и за предыдущий цикл, но пока так, и типа по действиям)
peoples_graph = deepcopy(peoples_simple)
for people, friends in peoples_simple.items():
    for friend in friends:
        if friend not in peoples_graph:
            peoples_graph[friend] = [people, ]
        elif people not in peoples_graph[friend]:
            peoples_graph[friend].append(people)
# print(*peoples_graph.items(), sep='\n')

# 1 задание
first_invited = 'Вячеслав Васин'
lengths = bfs(peoples_graph, first_invited)
# для bfs можно задать более жесткие условия типа dist < 3
num_guests = len([dist for dist in lengths.values() if dist is not None])
print(f"Придет {num_guests} человек, если отправить приглашение на имя {first_invited}. (Всего людей в базе {len(peoples_graph)})")

# 2 задание
# выбираем любую начальую точку и делаем проход от нее
count = 1
peoples_list = list(peoples_graph.keys())
visited = dfs(peoples_graph, peoples_list[0])
not_visited = {people for people, is_visited in visited.items() if is_visited is None}
while not_visited:
    # берем любую точку из непосещенных, и обходим заново
    visited = dfs(peoples_graph, not_visited.pop())
    # обновляем множество непосещенных по результатам очередного прохода
    not_visited -= {people for people, is_visited in visited.items() if is_visited is not None}
    count += 1
print(f"Нужно пригласить как минимум {count} людей, чтобы пришли ВСЕ люди из базы. (Всего людей в базе {len(peoples_graph)})")
