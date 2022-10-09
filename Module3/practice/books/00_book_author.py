class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

print(book.author.surname)
