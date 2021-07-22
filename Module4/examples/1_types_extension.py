# ================================
#   Расширение встроенных типов
# ================================


# Расширяем стандартный class dict
class my_dict(dict):
    # Добавляем свой метод
    def new_method(self):
        return "I'm new_method"

    # Добавляем дополнительный функционал к существующему методу
    def __setitem__(self, key, value):
        print('Setting %r to %r' % (key, value))
        return super().__setitem__(key, value)


m_dict = my_dict({1: 2, 2: 3})
print(m_dict)

# Данная операция вызывает метод __setitem__
m_dict["new_key"] = "new_value"
print(m_dict)

# print(m_dict.keys())

print(m_dict.new_method())

print("\n***Demo MyList****")


class MyList(list):
    """
    Список, индексы которого начинатся с 1, а не с 0
    """
    def __getitem__(self, offset):
        print('(indexing % s at % s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

x = MyList('abc')  # __init__ наследуется из списка
print(x)  # __repr__ наследуется из списка

print(x[1])  # MyList.__getitem__
print(x[3])  # Изменяет поведение метода суперкласса

x.append('spam')
print(x)  # Атрибуты, унаследованные от суперкласса list
x.reverse()
print(x)
