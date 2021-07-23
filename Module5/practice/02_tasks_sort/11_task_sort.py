# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
import pprint

words = ['step', 'name', 'pest', 'curtis', 'ocean', 'citrus', 'meal', 'printer', 'male', 'lemon',
         'mouse', 'melon', 'vase', 'flash', 'save']
anagram_list = []
while len(words) > 1:
    first_word = words.pop(0)
    for word in words:
        if set(first_word) == set(word):
            anagram_list.append(f'{first_word} - {word}')
            words.remove(word)
print('Список анаграмм: ')
pprint.pprint(anagram_list)
