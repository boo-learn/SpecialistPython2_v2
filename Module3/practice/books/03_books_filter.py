class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        return f'{self.name[0]}.{self.surname}'


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        return f'"{self.name}" author:{self.author.short_name()} publish:{self.year}' 


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
author_books = []
for num, book in enumerate (books_catalog, 1):    
    if book.author.surname.lower() == surname.lower():
        author_books.append(book.name)
if not author_books:
    print('Книги не найдены')
else:
    for num, book in enumerate(author_books, 1):
        print(num, book)
