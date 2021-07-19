# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

words = ['мать', 'тьма', 'маяк', 'ямка', 'лось', 'соль', 'тест', 'маяк', 'тьма']
w_copy = []
for word in words:
    w_copy.append(sorted(word))
anagram_idx = []
for i, word_target in enumerate(w_copy):
    res_str = words[i]
    was_found = False
    for j, word_equal in enumerate(w_copy):
        if j > i and word_target == word_equal and j not in anagram_idx:
            res_str += ' ' + words[j]
            anagram_idx.append(j)
            was_found = True
    if was_found:
        print(res_str)
