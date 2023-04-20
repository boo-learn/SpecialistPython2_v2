# 03_books_filter.py

class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        return self.name[0]+"."+self.surname


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        return '"'+ self.name+'" author: '+ self.author.short_name() + ' publish: ' + str(self.year) + ' год'


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
# TODO-1: Выведите нумерованный список книг автора с фамилией surname
#  примечание: если книг для автора с указанной фамилией нет - выведите "Книги не найдены"
book_find = False
for num, book in enumerate(books_catalog,1):
    if book.author.surname == surname:
        print(num, '\t|', book.to_str())
        book_find = True
if book_find == False: print("Книги не найдены")
