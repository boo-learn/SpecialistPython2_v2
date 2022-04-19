# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
def anagrams(words):
    words_sorted = words.copy()  # копируем массив для дажьнейшей обработки
    for i in range(len(words_sorted)):
        words_sorted[i] = sorted(words_sorted[i])  # сортируем слова посимвольно
    index_dict = {}  # создаем словарь (словарь - сразу для того чтобы избавиться от повторов)
    for i in range(len(words_sorted)):
        for j in range(i + 1, len(words_sorted)):
            if words_sorted[i] == words_sorted[j]:  # заполняем словарь - при нахождении повторов они прсто
                # проапдейтятся
                index_dict.update({i: None})
                index_dict.update({j: None})
    for el in list(index_dict.keys()):
        print(words[el]) # выводим список анаграмм


words = ['lav', 'log', 'val', 'gol', 'valle', ' ', 'log']
anagrams(words)
