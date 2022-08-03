# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы 
# (слова, составленные из одних и тех же букв).
from collections import defaultdict


def flatten(items) -> list:
    return [inner for item in items for inner in item]


def anagrams(words) -> list:
    """"
    Находит анаграммы в списке слов
    :param words: слова
    :return: список анаграмм
    """
    get_letters = lambda x: ''.join(sorted(word.lower()))
    my_dict = defaultdict(list)
    for word in words:
        my_dict[get_letters(word)].append(word)
    anagrams = list(filter(lambda x: len(x) > 1, my_dict.values()))
    return flatten(anagrams)
    

res = anagrams(['Аня', 'Яна1', 'кот1', 'ток', 'мяч', 'проверка', 'проверкаа'])
print(*res)
