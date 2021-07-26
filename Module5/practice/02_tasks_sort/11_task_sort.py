# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

worlds=["кот","тик","ток","кто","тир","кит"]
sort_char=[]
for world in worlds:
    sort_char.append(sorted(world))
print(sort_char)
for el in sort_char:
    if sort_char.count(el)>1:
        my_worlds = []
        for i in range(sort_char.count(el)):
            my_index=sort_char.index(el)
            my_worlds.append(worlds[my_index])
            worlds.remove(worlds[my_index])
            sort_char.remove(el)
        print(my_worlds)
