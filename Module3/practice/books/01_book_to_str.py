class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def short_name(self):
        # TODO-1: метод возвращает строку в формате: М.Булгаков
        #  пояснение: Первую букву имени, фамилию целиком
        first_initial = self.name[0]
        return first_initial


class Book:
    def __init__(self, name, author: Author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self):
        # TODO-2: метод возвращает строку в формате: "Вьюга" author:М.Булгаков publish:1926 год
        #  пояснение: Название книги выводим в кавычках(""), у имени автора только первую букву
        var1 = f'"{self.name}" author: {author.short_name()} {self.author.surname} published: {self.year}'
        return var1


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
print(book.to_str())
