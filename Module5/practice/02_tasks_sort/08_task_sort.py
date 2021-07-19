from pprint import pprint
# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
phones_tokenized = []
for phone in phones:
    phones_tokenized.append(phone.split('-'))
phones_tokenized.sort(key=lambda el: (el[0], el[1], el[2]))
pprint(phones_tokenized)
