class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Класс для связанного однонаправленного списка.
    """
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.current = None
        self.length = 0
        for arg in args:
            self.add(arg)

    def __str__(self):
        # убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ', ' + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def __len__(self):
        # сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        return self.length

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

    def __getitem__(self, item):
        current = self.first
        index = 0
        while current is not None:
            if index == item or (index - len(self)) == item:
                return current.value
            current = current.next
            index += 1
        raise IndexError(f"Элемент со индексом {item} не существует в списке {self}")

    def __setitem__(self, key, value):
        current = self.first
        index = 0
        while current is not None:
            if index == key:
                current.value = value
                return
            current = current.next
            index += 1
        raise IndexError(f"Элемент со индексом {key} не существует в списке {self}")

    def __delitem__(self, key):
        prev_node = self.first
        current_node = self.first
        while current_node is not None:
            if key == 0 or key == -len(self):
                self.first = current_node.next
                self.length -= 1
                return
            elif key > len(self) - 1 or key < -len(self):
                raise IndexError(f"Элемент со индексом {key} не существует в списке {self}")
            else:
                for i in range(len(self)):
                    if i == key or (i - len(self) == key):
                        prev_node.next = current_node.next
                        self.length -= 1
                        return
                    prev_node = current_node
                    current_node = current_node.next

    def clear(self):
        """
        Очищаем список
        """
        # реализовать очистку списка
        self.__init__()

    def remove(self, value):
        """
        Ищет элемент со зачением value и удаляет его
        :param value: значение удаляемого элемента
        :return: ValueError, если элемент не найден
        """
        current = self.first
        index = 0
        while current is not None:
            if current.value == value:
                del self[index]
                self.length -= 1
                return
            current = current.next
            index += 1
        raise ValueError(f"Элемент со значением {value} не найден")

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        # Создаем новый узел
        new_node = Node(value, None)
        if self.first is None:
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = new_node
            self.length += 1
        else:
            # здесь, уже на разные
            new_node = Node(value, None)
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
            self.length += 1
        else:
            new_node = Node(value, self.first)
            self.first = new_node
            self.length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        # реализовать вставку
        prev_node = self.first
        current_node = self.first
        current_index = 0
        if index == 0:
            self.push(value)
            return
        if index > len(self):
            self.add(value)
            return
        while current_node.next is not None:
            current_node = current_node.next
            current_index += 1
            if current_index == index - 1:
                prev_node = current_node
        new_node = Node(value, prev_node.next)
        prev_node.next = new_node

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ValueError, если элемент не найден
        """
        # реализовать поиск элемента
        # подумать над возвращаемым значением, если элемент со значение value не найден
        current = self.first
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        raise ValueError(f"Элемент со значением {value} не найден")

    def reverse(self):
        """
        Разворачивает связанный список (Значение первой ноды становится значением последней,
        значение второй ноды - значением предпоследней, и т.д.)
        """
        temp = LinkedList()
        for i in range(len(self)):
            temp.add(self[-i - 1])
        self.clear()
        for i in range(len(temp)):
            self.add(temp[i])


if __name__ == "__main__":
    # Проверка создания списка (.add, .push, .insert) и расчета длины списка (len())
    L = LinkedList()
    print("empty list = ", L)
    print(f'{len(L)=}')
    L.add(1)
    L.add(2)
    L.add(3)
    L.push(0)
    L.insert(-5, 5)
    print("list = ", L)
    print(f'{len(L)=}')

    print('*'*40)
    # Проверка поиска индекса по значению (.find)
    try:
        searched_number_index = L.find(-5)
        print(f'{searched_number_index = }')
    except ValueError as e:
        print(e)

    print('*'*40)
    # Проверка интерфейса итерации (iter, next)
    for el in L:
        print(el)
    # print(f'{sum(L)}')
    # print(f'{max(L)}')
    # print(f'{list(map(str, L))}')
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    print('*'*40)
    # Проверка обращения и изменения значения по индексу (в т.ч. обработка отрицательных значений индекса)
    # (getitem, setitem)
    try:
        print(L[0])
    except IndexError as e:
        print(e)
    L[0] = "new"
    print(L[0])
    print(L)
    print(f'{L[-2]=}')

    print('*'*40)
    # Проверка создания нового списка с указанием начальных элементов:
    L = LinkedList(2, 4, 6, -12)
    print(L)

    print('*'*40)
    # Проверка очистки списка (clear) и удаления элементов по индексу (del), по значению (.remove) :
    print(L)
    del L[3]
    del L[-1]
    print(L)
    try:
        L.remove(2)
    except ValueError as e:
        print(e)
    print(L)
    L.clear()
    print(L)
    print(len(L))

    print('*'*40)
    # Проверка обращения (разворота) списка (.reverse)
    L = LinkedList(2, 4, 6, -12)
    print(L)
    L.reverse()
    print(L)
