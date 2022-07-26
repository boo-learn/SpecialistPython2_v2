class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        return self.name[0] +"."+ self.surname


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        return f'"{self.name}" author: {self.author.short_name()} publish:{self.year}'


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)
print (author.short_name());
# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
print(book.to_str())
author = Author("Иван", "Булаков")
book = Book("Вьюга", author, 1926, 25)
print(book.to_str())
