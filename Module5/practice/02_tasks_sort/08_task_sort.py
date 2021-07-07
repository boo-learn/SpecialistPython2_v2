from functools import reduce
# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]


def sort_phone(phone: str):
    list_int = [int(val) for val in phone.split('-')]
    list_int[0] = list_int[0]*1000
    list_int[1] = list_int[1]*10
    return reduce(lambda x, y: x+y, list_int)


if __name__ == '__main__':
    print(sorted(phones, key=lambda val: sort_phone(val)))
