class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        return f"{self.name[0]}. {self.surname}"


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        return f"{self.name} author: {self.author.short_name()} publish: {self.year} год"


author1 = Author("Михаил", "Булгаков")
author2 = Author(name="Стивен", surname="Кинг")

books_catalog = [
    Book("Вьюга", author1, 1926, 25),
    Book("Мастер и Маргарита", author1, 1967, 480),
    Book("Собачье сердце", author1, 1987, 352),
    Book("Сияние", author2, 2014, 544),
    Book("Оно", author2, 1986, 320),
]
print("Найти все книги по фамилии автора")
surname = input("Фамилия автора: ")
delta = 0
a = []
for num, book in enumerate(books_catalog, 1):
    if book.author.surname == surname:
        print(num, book.to_str())
        delta += 1
if delta == 0:
    print("Книги не найдены")
# TODO-1: Выведите нумерованный список книг автора с фамилией surname
#  примечание: если книг для автора с указанной фамилией нет - выведите "Книги не найдены"
