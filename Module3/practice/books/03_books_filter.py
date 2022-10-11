class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        return self.name[0] +"." + self.surname
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком

class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        return '"{}". Автор: {}. Публикация в {} году'.format(self.name,self.author.short_name(),self.year)
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву


author1 = Author("Михаил", "Булгаков")
author2 = Author(name="Стивен", surname="Кинг")

books_catalog = [
    Book("Вьюга", author1, 1926, 25),
    Book("Мастер и Маргарита", author1, 1967, 480),
    Book("Собачье сердце", author1, 1987, 352),
    Book("Сияние", author2, 2014, 544),
    Book("Оно", author2, 1986, 320),
]
for i, val in enumerate(books_catalog, start=1):
    if author1.surname==val.author.surname:
        print(f'№ {i}  {val.to_str()}')

