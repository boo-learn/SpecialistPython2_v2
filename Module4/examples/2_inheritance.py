# Наследование подразумевает, что дочерний класс содержит все атрибуты родительского класса,
# при этом некоторые из них могут быть переопределены или добавлены в дочернем.


# Рассмотрим два класса
class Student:
    def __init__(self, name, surname, birth_date, school, class_room):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


class Teacher:
    def __init__(self, name, surname, birth_date, school, teach_classes):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self.teach_classes = list(map(self.convert_class, teach_classes))

    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name

# Эти Классы описывают два различных объекта
# Но часть информации у них общая(атрибуты, методы)


# Общую информацию выносим в Класс-предок (родитель)
class People:
    def __init__(self, name, surname, birth_date, school):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


# Сами классы наследуем
class Student(People):
    def __init__(self, name, surname, birth_date, school, class_room):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, surname, birth_date, school)
        # Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # И уникальные методы
    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(People):
    def __init__(self, name, surname, birth_date, school, teach_classes):
        People.__init__(self, name, surname, birth_date, school)
        self.teach_classes = list(map(self.convert_class, teach_classes))

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

# Наследование позволяет избежать дублирования и кода
        # и повторно использовать уже готовые реализации