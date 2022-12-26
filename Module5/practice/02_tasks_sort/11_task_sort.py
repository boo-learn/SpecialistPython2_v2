# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

input_words = ['слово', 'импортер', 'австралопитек', 'кит', 'кот', 'ватерполистка', 'автор', 'пирометр', 'ротор',
               'терпеливость', 'ток', 'товар', 'тик', 'реимпорт', 'просветитель', 'расточительство', 'рвота', ]

key_func = lambda word: str(sorted(word))

# решение без groupby
anagrams = dict()
for word in input_words:
    key = key_func(word)
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word, ]
for words in anagrams.values():
    if len(words) > 1:
        print(words)

print('\n*****\n')

# решение c groupby
import itertools


input_words.sort(key=key_func)
for key, group_item in itertools.groupby(input_words, key=key_func):
    words = list(group_item)
    if len(words) > 1:
        print(words)


