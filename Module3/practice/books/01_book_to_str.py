

class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком
        return f'{self.name[0]}. {self.surname}'


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        ...
        return f'"{self.name}" author: {author.short_name()} publish: {book.year} год'


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)
print(author.short_name())

# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
author = Author("Афанасий", "Фет")
book = Book("Чума", author, 1901, 250)

print(book.to_str())
