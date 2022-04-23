# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

def make_sorted_list(word):
    letters = list(word.lower())
    letters.sort()
    return letters


if __name__ == "__main__":
    dictionary = ["слово", "волос", "трата"]
    dictionary_sorted = []
    dictionary_annagramms = []
    for word in dictionary:
        dictionary_sorted.append(make_sorted_list(word))
    for word in dictionary:
        if dictionary_sorted.count(make_sorted_list(word)) > 1 and word not in dictionary_annagramms:
            dictionary_annagramms.append(word)
    print(dictionary_annagramms)
