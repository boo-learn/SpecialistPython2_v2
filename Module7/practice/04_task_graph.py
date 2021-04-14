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


def full_name(my_dict):
    return f"{my_dict['surname']} {my_dict['name']}"


def dfs(graph, v):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(v)
    return visited


with open('peoples.json', encoding="utf-8") as f:
    people = json.load(f)

people_list = []
for man in people:
    if not full_name(man) in people_list:
        people_list.append(full_name(man))
    for friend in man['friends']:
        if not full_name(friend) in people_list:
            people_list.append(full_name(friend))

print(people_list)

people_graph = []
for _ in range(len(people_list)):
    people_graph.append([])
for man in people:
    man_num = people_list.index(full_name(man))
    for friend in man['friends']:
        friend_num = people_list.index(full_name(friend))
        if not (friend_num in people_graph[man_num]):
            people_graph[man_num].append(friend_num)
            people_graph[friend_num].append(man_num)

print(people_graph)
# people_graph.append([19])
# people_graph.append([18])
# people_graph.append([21])
# people_graph.append([20])

send_invitation = input("Введите фамилию и имя человека, кому мы собираемся направить приглашение: ")
if send_invitation in people_list:
    invited = dfs(people_graph, people_list.index(send_invitation))
    print (f'Если приглашение получит {send_invitation}, к нам придет {sum(invited)} человек')
else:
    print(f'Ошибка: "{send_invitation}" в списке людей не найден')

step = 1
send_invitation = 0
invited = dfs(people_graph, send_invitation)
while sum(invited) != len(invited):
    send_invitation = invited.index(False)
    new_invited = dfs(people_graph, send_invitation)
    for i in range(len(invited)):
        invited[i] += new_invited[i]
    step += 1

print(f'Минимальное количество людей для отправки приглашения: {step}')
