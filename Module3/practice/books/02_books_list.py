class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        return self.name[0]


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        return f'"{self.name}" author: {self.author.short_name()}.{self.author.surname} published: {self.year} год'


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
for n, book in enumerate(books_catalog):
    print(f"{n}. {book.to_str()}")
