class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        return self.name[0] + '.' + self.surname


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        return f'"{self.name}" author:{self.author.short_name()} publish:{self.year} год'


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

author = Author("Александр", "Пешкин")
book = Book("Солома", author, 1926, 25)
# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
print(book.to_str())
