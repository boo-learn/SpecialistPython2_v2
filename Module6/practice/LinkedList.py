class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, *args):
        if args:
            self.first = self.last = Node(args[0], None)
            for el in args[1:]:
                self.add(el)
        else:
            self.first = None
            self.last = None

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            return out[:-1] + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
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
        # TODO: реализовать вставку
        count = 0
        node = self.first
        if index == 0:
            self.push(value)
        while node.next:
            if count == index-1:
                new_node = Node(value, node.next)
                node.next = new_node
                return
            count += 1
            node = node.next
        self.add(value)

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        count = 0
        node = self.first
        while node:
            if node.value == value:
                return count
            count += 1
            node = node.next
        return -1

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        length = 0
        if self.first is not self.last:
            current = self.first
            while current.next is not self.last:
                current = current.next
                length += 1
        return length + 2  # +1 для учета self.first

    def __iter__(self):
        node = self.first
        while node:
            yield node
            node = node.next

    def __getitem__(self, item):
        count = 0
        node = self.first
        while node.next:
            if count == item:
                return node.value
            count += 1
            node = node.next

    def __setitem__(self, key, value):
        count = 0
        node = self.first
        while node.next:
            if count == key:
                node.value = value
            count += 1
            node = node.next


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)
    L.insert(5, 2)
    print("list = ", L)
    print(f'нахождение ноды со значением 5 {L.find(5)}')
    print(f'длина списка {L.len()}')
    for el in L:
        print(el.value)
    print(f'значение элемента с индексом 2 {L[2]}')
    L[2] = 25
    print(f'измененный по индексу список {L}')
    T_L = LinkedList(2, 4, 'new', 47)
    print(T_L)
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
