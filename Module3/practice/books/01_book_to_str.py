class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком
        return f'{self.name[0]}.{self.surname}'


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        return f'"{book.name}" author:{author.short_name()} publish: {book.year} год.'


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями

print(author.short_name())
print(book.to_str())

author.name = input('Bведите имя автора: ').title()
author.surname = input('Bведите фамилию автора: ').title()
book.name = input('Bведите название книги: ').title()

print(book.to_str())
