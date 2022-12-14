# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

i = 0

while i < len(phones) - 1:
    m = i
    j = i + 1
    while j < len(phones):
        if phones[j] < phones[m]:
            m = j
        j += 1
    phones[i], phones[m] = phones[m], phones[i]
    i += 1

print(phones)
