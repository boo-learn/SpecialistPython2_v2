class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        ...
        return f"{self.name[0]}.{self.surname}"


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        ...
        return f'"{self.name}" author:{book.author.short_name()} publish:{self.year}'


author1 = Author("Михаил", "Булгаков")
author2 = Author(name="Стивен", surname="Кинг")

books_catalog = [
    Book("Вьюга", author1, 1926, 25),
    Book("Мастер и Маргарита", author1, 1967, 480),
    Book("Собачье сердце", author1, 1987, 352),
    Book("Сияние", author2, 2014, 544),
    Book("Оно", author2, 1986, 320),
]

# TODO-1: Выведите нумерованный список книг, используя для каждой книги ее строковое представление(метод .to_str())
n = 1
for book in books_catalog:
    print(f'{n}.{book.to_str()}')
    n += 1
