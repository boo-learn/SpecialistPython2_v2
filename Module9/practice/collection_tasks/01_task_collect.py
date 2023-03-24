import collections

counter = collections.Counter()

free_text = "Частотный анализ — это подсчёт, какие символы чаще встречаются в тексте. Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря до шифровальной машины «Энигма»"

for word in free_text:
    counter[word] += 1

print(counter)
