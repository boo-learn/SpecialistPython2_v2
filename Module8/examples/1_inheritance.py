# Рассмотрим два класса
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"


class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def greet(self):
        return f"Hi, it's {self.name}"

    def my_job(self):
        return f"I'm {self.job_title}"


# Эти Классы описывают два различных типа объектов
# Часть информации у них общая(атрибуты, методы), а часть отличается


# Чтобы избежать дублирования кода, воспользуемся наследованием.
# Наследуем класс Employee от Person:
class Employee(Person):
    def __init__(self, name, job_title):
        # Вызываем конструктор родителя, чтобы создать атрибут .name
        super().__init__(name)
        # Добавляем новый атрибут, которого не было у родителя:
        self.job_title = job_title

    # Метод greet() - описывать не нужно, он будет унаследован от родителя

    # Описываем новый метод, которого не было у родителя:
    def my_job(self):
        return f"I'm {self.job_title}"
