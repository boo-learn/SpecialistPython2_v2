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


author1 = Author("Михаил", "Булгаков")
author2 = Author(name="Стивен", surname="Кинг")

books_catalog = [
    Book("Вьюга", author1, 1926, 25),
    Book("Мастер и Маргарита", author1, 1967, 480),
    Book("Собачье сердце", author1, 1987, 352),
    Book("Сияние", author2, 2014, 544),
    Book("Оно", author2, 1986, 320),
]
print("Найти все книги по фамилии автора")
surname = input("Фамилия автора: ")

count = 0
for book in books_catalog:
    if book.author.surname.lower() == surname.lower():
        count += 1
        print(f'{count}. {book.name}')
if count == 0:
    print('Книги не найдены')
