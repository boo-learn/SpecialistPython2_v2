# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

words = ['камень', 'береза', 'Василий', 'лунь', 'мошкара', 'ромашка', 'удар', 'руда']

for wrd1 in words:
    for wrd2 in words:
        if len(wrd1)==len(wrd2) and wrd1 != wrd2:
            wrd1_sorted = sorted(wrd1.lower())
            wrd2_sorted = sorted(wrd2.lower())
            if wrd1_sorted == wrd2_sorted:
                print(f'{wrd1}')
