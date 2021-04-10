# Анаграммы*
# Задается словарь (список слов). Найти в нем все анаграммы (слова, составленные из одних и тех же букв).

words = ['qwerty', 'ytrewq', 'wasd', 'sadw', 'zxc', 'vbnm', 'rtyuiqw', 'qwer', 'werqty', 'czx', 'y6u6', '6yu6']
tmp_check = {}
result = []

while words:
    tmp_check = tmp_check.fromkeys(words[0])
    for word in words:
        if tmp_check == dict.fromkeys(word):
            result.append(word)
    if len(result) == 1:
        pass
    else:
        print('*' * 40)
        print(*result)
    for word in result:
        words.remove(word)
    result = []
