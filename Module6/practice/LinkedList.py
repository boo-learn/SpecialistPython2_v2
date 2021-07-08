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

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out +=',' + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self.first = None
        self.last = None

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

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if (self.first is not None) and (0 < index < len(self)):
            new_node = Node(value, None)
            i = 1
            current = self.first
            while i != index:
                current = current.next
                i += 1
            new_node.next=current.next
            current.next=new_node
        else:
            raise TypeError("index out of range")

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        raise TypeError("Not implemented")

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)

    # TODO: реализовать интерфейс итерации
    # for el in L:
    #     print(el)
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
