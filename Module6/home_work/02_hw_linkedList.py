# Для Связанного списка(LinkedList) реализуйте метод reverse() - меняющий значения всех нод(узлов) на противоположное.
# Значение первой ноды становится значением последней, значение второй, значением предпоследней.
# Примечание: при реализации не используйте список(list).
class Node:
    """Класс для узла списка. Хранит значение и указатель на следующий узел."""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'Node: {self.value}'


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.elem_index = 0
        if args:
            for arg in args:
                self.__add__(arg)
        self.length = None
        self.length = self.__len__()

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            return out[:-1] + ']'
        return 'LinkedList []'

    def __add__(self, other):
        self.add(other)

    def __iter__(self):
        self.elem_index = 0
        return self

    def __next__(self):
        node = self.__getitem__(self.elem_index)
        self.elem_index += 1
        if self.elem_index > self.__len__():
            raise StopIteration
        return node

    def __getitem__(self, index):
        i = 0
        if index > len(self):
            raise IndexError
        node = self.first
        while i != index:
            node = node.next
            i += 1
        return node

    def __setitem__(self, key, value):
        item = self.__getitem__(key)
        item.value = value

    def __len__(self):
        return self.len()

    def __reversed__(self):
        return self.reverse()

    def clear(self):
        """Очищаем список"""
        self.first = None
        self.last = None
        self.length = 0

    def add(self, value):
        """Добавляем новое значение value в конец списка"""
        self.length = None
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length = self.__len__()

    def push(self, value):
        """Добавляет элемент со значением value в начало списка"""
        self.length = 0
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node
        self.length = self.__len__()

    def insert(self, value, index):
        """Вставляет узел со значением value на позицию index"""
        item = self.__getitem__(index)
        item.value = value

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        i = 0
        node = self.first
        while i != self.__len__():
            if node.value == value:
                return i
            node = node.next
            i += 1
        raise AttributeError

    def len(self):
        if self.length:
            return self.length
        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        else:
            return 0
        return length + 1  # +1 для учета self.first

    def reverse(self):
        for i in range(self.__len__() // 2):
            self[i].value, self[self.__len__() - i - 1].value = self[self.__len__() - i - 1].value, self[i].value
        return self


if __name__ == "__main__":
    L = LinkedList(2, 4, 6, -12, 8)
    print(L)
    # print(len(L))

    print('reverse()')
    L.reverse()
    print(L)
    print(reversed(L))
    L.add(100)
    print(reversed(L))
    print(L.first)
    print(L.last)
