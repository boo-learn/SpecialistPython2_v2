
# Задача
# По предоставленным данным(файл peoples.json) определите:
# 1. Сколько людей придет на открытие, если вы отправляете приглашение конкретному человеку
# (любому, на ваш выбор, из базы), а тот всем друзьям, друзья друзьям и т.д.

# 2. Какому минимальному числу людей, нужно отправить приглашение,
# чтобы пришли ВСЕ люди, присутствующие в базе?


# Сюда отправляем полное решение

# По задачам - у меня получилось:
# 1. Придут все, кому бы ни отправить приглашение.
# 2. Соответственно - минимальное одно приглашение любому человеку.
#


import json
from pprint import pprint

def search_in_friends(graph, start):
    friendship = dict.fromkeys(graph.keys(), None)
    friendship[start] = 0  # "Дальность" от начала до друга
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if friendship[vertex] is None:
                friendship[vertex] = friendship[cur_vertex] + 1
                queue.append(vertex)
    return friendship

def create_vertexes_from_peoples(peoples):
    """Создаю словарь с ключами в виде имени фамилии каждого человека"""
    keys = []
    for man in peoples:
        keys.append((man['name'], man['surname']))
        for friend in man['friends']:
            keys.append((friend['name'], friend['surname']))
    vertexes = dict.fromkeys(keys, None)
    return vertexes

def create_graph(vertexes, peoples):
    """Создаю граф"""
    for people in peoples:
        people_name = (people['name'], people['surname'])
        
        # Если человек в верхнем уровне - его друзья указаны в ключе 'friends'
        vertexes[people_name] = [(friend['name'], friend['surname']) for friend in people['friends']]
        
        for friend in people['friends']:
            
            # А теперь обратно - для каждого человека из списка 'friends' по одноименному ключу
            # добавляю человека верхнего уровня в связь
            friend_name = (friend['name'], friend['surname'])
            
            # Если человек попадается впервые - создаю у него пустой список
            if not vertexes[friend_name]:
                vertexes[friend_name] = []
                
            # Проверяю дублирование людей на случай еси два человека имеют общих знакомых
            # через несколько друзей
            if people_name not in vertexes[friend_name]:
                vertexes[friend_name].append(people_name)
    return vertexes
    

file = open('peoples.json', encoding='utf8')
peoples = json.load(file)
file.close()
vertexes = create_vertexes_from_peoples(peoples)
graph = create_graph(vertexes, peoples)
friendship = search_in_friends(graph, ('Иван', 'Гриб'))
pprint(friendship)
