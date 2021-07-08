class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ',' + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def __iter__(self):
        self.current_iter = self.first
        return self

    def __next__(self):
        if self.current_iter.next is not None:
            self.current_iter = self.current_iter.next
            # return self.current_iter.value
        else:
            raise StopIteration

    def clear(self):
        """
        Очищаем список
        """
        self.first = self.last = None

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node
        self.length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index == 0:
            self.push(value)
            self.length += 1
            return

        cntr = 1
        if self.first is not None:
            current = self.first
            while current.next is not None:
                if index == cntr:
                    new_node = Node(value, current.next)
                    current.next = new_node
                    self.length += 1
                    return
                cntr += 1
                current = current.next
        raise TypeError("Index error")

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        index = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                if current.value == value:
                    return index
                current = current.next
                index += 1
        return -1

    def len(self):
        return self.length


# if __name__ == "__main__":
L = LinkedList()
print("empty list = ", L)
L.add(1)
L.add(2)
L.add(3)
L.insert(4, 2)

print("list = ", L)
# L.clear()
# print("list = ", L)
# print(L.find(2))
# print(L.find(8))

# TODO: реализовать интерфейс итерации
for el in L:
    print(el)
# Напомню принцип работы итератора:
# iterator_L = iter(L) L.__iter__()
# next(iterator_L) it.__next__()
# next(iterator_L)
# next(iterator_L)
# next(iterator_L)

# TODO: реализовать обращение по индексу и изменение значение по индексу
# print(L[0])
# L[0] = "new"
# print(L[0])

# TODO: реализовать создание нового списка с задание начальных элементов
# L = LinkedList(2, 4, 6, -12)
# print(L)
