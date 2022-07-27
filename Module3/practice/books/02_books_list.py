class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком
        return f"{self.name[0]}.{self.surname}"


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        return f'"{self.name}" author: {self.author.name[0]}.{self.author.surname}. publish: {self.year} год'
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        ...


# author = Author("Михаил", "Булгаков")
# author2 = Author("Лев", "Толстой")
# book = Book("Вьюга", author, 1926, 25)
# book2 = Book("Война и мир", author2, 1900, 2500)
# 
# # TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
# print(book.to_str())
# print(book2.to_str())
# print(author2.short_name())
# print(author.short_name())

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
i = 1
for book in books_catalog:
    print(f'{i}. {book.to_str()}')
    i += 1
