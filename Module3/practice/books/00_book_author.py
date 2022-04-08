class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

print(book.author.surname)