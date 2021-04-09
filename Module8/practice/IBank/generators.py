from random import randint


def get_user_data():
    names = ["Иван", "Петр", "Алексей"]
    second_names = ["Петрович", "Федорович", "Алексеевич", "Эдуардович"]
    surnames = ["Кукуев", "Гарный", "Клинов", "Цой"]
    return names[randint(0, len(names) - 1)], second_names[randint(0, len(second_names) - 1)], \
           surnames[randint(0, len(surnames) - 1)], randint(10000000, 100000000), \
           f"+7-9{randint(10, 100)}-{randint(100, 1000)}-{randint(10, 100)}-{randint(10, 100)}"


if __name__ == "__main__":
    print(get_user_data())
    print(get_user_data())
    print(get_user_data())
