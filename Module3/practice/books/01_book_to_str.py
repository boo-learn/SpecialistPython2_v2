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
        return f'{self.name} author: {author.short_name()} publish: {self.year} год'

author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)
#x = author.short_name()
print(author.short_name())
print(book.to_str())
