# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

anagrams = ['рамка', 'НОС', 'АТЛаС', 'ЧУГУН', 'сОН', 'САЛАТ', 'Корова', 'МаРКА']

for i in range(len(anagrams)):
    for j in range(i+1, len(anagrams)):
        if sorted(list(anagrams[i].lower())) == sorted(list(anagrams[j].lower())):
            print(f"{anagrams[i]} - {anagrams[j]}")
