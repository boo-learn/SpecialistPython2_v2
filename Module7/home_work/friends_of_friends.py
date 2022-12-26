# "Друзья друзей"
#  У всех людей, по крайне мере я надеюсь, есть друзья. У ваших друзей
#  тоже есть друзья и так далее.
#  Вы решили запустить свой бизнес и пригласить максимальное количество
#  людей на его открытие. Вам в руки попала, как нельзя кстати,
#  база людей со списком их друзей. Считаем, что комбинация Имя+Фамилия
#  нам позволяет однозначно идентифицировать человека.
# Задача
# По предоставленным данным(файл peoples.json) определите:
# 1. Сколько людей придет на открытие, если вы отправляете приглашение
# конкретному человеку (любому, на ваш выбор, из базы), а тот всем
# друзьям, друзья друзьям и т.д.
# 2. Какому минимальному числу людей, нужно отправить приглашение,
# чтобы пришли ВСЕ люди, присутствующие в базе?

import json


def get_names(file_path) -> list:
    """
    Получает список друзей из файла
    :return: Список друзей
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def dfs_friends_all_list(friends) -> list:
    """
    Обходит весь список друзей
    :return: список всех друзей
    """
    visited = []

    def _dfs_friends(friends):
        for friend in friends:
            name = '  '.join([friend['name'], friend['surname']])
            if name not in visited:
                visited.append(name)
            if 'friends' in friend.keys():
                _dfs_friends(friend['friends'])
    _dfs_friends(friends)
    return visited


def dfs_friends(v, friends) -> list:
    """
    Обходит друзей, начиная с конкретного человека
    :return: список друзей, которых успел посетить
    """
    visited = []

    def find_in_friends(v):
        for friend in friends:
            if (friend['name'] == v['name'] and
                    friend['surname'] == v['surname']):
                return friend

    def _dfs_friends(v):
        name = '  '.join([v['name'], v['surname']])
        if name not in visited:
            visited.append(name)
            v = find_in_friends(v)
            if v and 'friends' in v.keys():
                for friend in v['friends']:
                    _dfs_friends(friend)

    _dfs_friends(v)
    return visited


def find_min(people, full_list) -> int:
    """
    Находит минимальное количество гостей
    :return: количество гостей
    """
    friends_of_friends = []
    for friend in people:
        name = '  '.join([friend['name'], friend['surname']])
        guests = dfs_friends(friend, people)
        friends_of_friends.append((name, guests))
    friends_of_friends.sort(key=lambda x: len(x[1]), reverse=True)
    guest_list = set()
    invitations = []
    for guest in full_list:
        if guest in guest_list:
            continue
        for name, friend_list in friends_of_friends:
            if guest in friend_list and name not in invitations:
                invitations.append(name)
                guest_list |= set(friend_list)
                continue
    print(f'Нужно пригласить: {", ".join(invitations)}')
    return len(invitations)


people = get_names('peoples.json')
full_list = dfs_friends_all_list(people)

for idx, name in enumerate(full_list):
    print(idx + 1, name)

trial1 = dfs_friends({'name': 'Вячеслав', 'surname': 'Иванов'}, people)
print()
print(len(trial1), trial1)

trial2 = dfs_friends({'name': 'Вячеслав', 'surname': 'Сидоров'}, people)
print()
print(len(trial2), trial2)
print(set(trial2) ^ set(full_list))

trial3 = dfs_friends({'name': 'Иван', 'surname': 'Гриб'}, people)
print()
print(len(trial3), trial3)

print()
print(find_min(people, full_list))
