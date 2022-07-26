class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        return f'{self.name[0]}. {self.surname}'
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком
        ...


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        return f'"{self.name}", author: {self.author.short_name()}, publish: {self.year}'
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        ...


author1 = Author("Михаил", "Булгаков")
author2 = Author("Александр", "Пушкин")
book1 = Book("Вьюга", author1, 1926, 25)
book2 = Book("Евгений Онегин", author2, 1883, 300)

# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
print(book1.to_str())
print(book2.to_str())
