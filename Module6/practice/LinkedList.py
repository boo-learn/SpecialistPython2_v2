class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.__ind = 0
        self.__current_iter_node = None
        self.__length = 0
        self.first = None
        self.last = None

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
        self.__current_iter_node = self.first
        return self

    def __next__(self):
        if self.__current_iter_node is None:
            raise StopIteration
        else:
            current = self.__current_iter_node
            self.__current_iter_node = self.__current_iter_node.next
            return current

    # def __getitem__(self, index):
    #     for i, node in enumerate.self:
    #         pass

    def clear(self):
        """
        Очищаем список
        """
        # current = self.first
        # while current is not None:
        #     temp = current
        #     current = current.next
        #     del temp
        # Using GC recursive link detecting.
        self.first = None
        self.last = None
        self.__length = 0

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
        self.__length += 1

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
        self.__length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        current = self.first
        for i in range(index+1):
            if current is None:
                raise IndexError("Index is out of list index range.")
            if i == index:
                new_node = Node(value, current.next)
                current.next = new_node

            else:
                current = current.next
        self.__length += 1

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или None, если элемент не найден
        """
        for i, node in enumerate(self):
            if node.value == value:
                return i
        return False

    def len(self):
        # length = 0
        # if self.first is not None:
        #     current = self.first
        #     while current.next is not None:
        #         current = current.next
        #         length += 1
        # else:
        #     return 0
        # return length + 1  # +1 для учета self.first
        return self.__length


if __name__ == "__main__":
    import sys
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)
    print("List", L, "has", L.len(), "nodes.")
    L.insert(0, 0)
    L.insert(2.5, 2)
    L.insert(L.len()-1, L.len()-1)
    # L.insert(1.5, 10) # Warning: raises an IndexError
    print("List", L, "has", L.len(), "nodes.")
    L.clear()
    print("List", L, "has", L.len(), "nodes after clearing.")
    L.add(1)
    L.add(2)
    L.add(2.5)
    L.add(3)
    for el in L:
         print(el)
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)
    print(f"2.5 is found in list at position {L.find(2.5)}.")
    if not L.find(999):
        print("999 not found in list!")
    # TODO: реализовать обращение по индексу и изменение значение по индексу
    # print(L[0])
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    # L = LinkedList(2, 4, 6, -12)
    # print(L)
