# =================================
#    Создание объектов-итераторов
# =================================


class IterObj:
    """
    Объект-итератор
    """
    def __init__(self, start=0):
        self.i = start
    # Объект считается итератором - если у него есть метод __next__

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class Iter:
    """
    Объект, поддерживающий интерфейс итерации
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # Метод __iter__ должен возвращать объект итератор
        return IterObj(self.start)

obj = Iter(start=2)

for el in obj:
    print(el)

print("Еще раз ...")
for el in obj:
    print(el)

print('sum(obj) -->', sum(obj))

# Функция map() возвращает объект-итератор
map_iter = map(int, '123')

print('next(map_iter) --> ', next(map_iter))
print('next(map_iter) --> ', next(map_iter))

# Цикл for..in продолжает перебор элементов, т.к. map_iter является итератором
for el in map_iter:
    print("el in for in -->", el)


class Iter2:
    def __init__(self, start=0):
        self.i = start

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


print("Demo Iter2")
obj = Iter2(start=2)

for el in obj:
    print(el)

print("Еще раз ...")
for el in obj:
    print(el)
