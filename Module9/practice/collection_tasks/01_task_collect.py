# Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте.
# Это важнейший инструмент взлома многих классических шифров —
# от шифра Цезаря до шифровальной машины «Энигма».
# Выполним простой частотный анализ: выясним, какой символ чаще всего
# встречается в данном тексте.


from collections import Counter


# Входные данные:
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore" \
       " magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea " \
       "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
       "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit " \
       "anim id est laborum."


if __name__ == '__main__':
    print('Частотный анализ')
    counter = Counter()
    for letter in text.replace(' ', ''):
        counter[letter] += 1
    print("counter=", counter)
    common = counter.most_common(1)[0]
    print(f'Самый часто встречающийся символ: {common[0]} в количестве {common[1]} раз(а)')
