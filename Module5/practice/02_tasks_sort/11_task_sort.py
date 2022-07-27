# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

words = ['abba', 'baba', 'dog', 'GOD', 'house', 'Dog']
d_words = dict()
for word in words:
    val = ''.join(sorted(word.lower()))
    if val not in d_words:
        d_words[val] = set()
    d_words[val].add(word.lower())
for k, v in d_words.items():
    if len(v) > 1:
        print(v)
