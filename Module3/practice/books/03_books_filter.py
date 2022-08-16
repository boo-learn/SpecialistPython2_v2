class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком
        return f"{self.name[0]}.{self.surname}"


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        return f'"{self.name}" author:{self.author.short_name()} publish:{self.year} год'


def get_all_to_str(books_catalog):
    print("Найти все книги по фамилии автора")
    surname = str(input("Фамилия автора: "))
    book_faund = False
    for book in books_catalog:
        if surname.upper() == book.author.surname.upper():
            print(book.to_str())
            book_faund = True
    if not book_faund:
        print(f"Книги автора {surname} не найдены")


author1 = Author("Михаил", "Булгаков")
author2 = Author(name="Стивен", surname="Кинг")

books_catalog = [
    Book("Вьюга", author1, 1926, 25),
    Book("Мастер и Маргарита", author1, 1967, 480),
    Book("Собачье сердце", author1, 1987, 352),
    Book("Сияние", author2, 2014, 544),
    Book("Оно", author2, 1986, 320),
]


get_all_to_str(books_catalog)
# TODO-1: Выведите нумерованный список книг автора с фамилией surname
#  примечание: если книг для автора с указанной фамилией нет - выведите "Книги не найдены"
