class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        return f'{self.name[0]}.{self.surname}'


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        return f'Книга: "{self.name}", Автор: {self.author.short_name()}, Издана: {self.year} год'


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

print(book.to_str())
