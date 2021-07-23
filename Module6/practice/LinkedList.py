class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.pointer = self.first
        self.limit = 0
        if len(args) > 0:
            for arg in args:
                self.add(arg)

    def __str__(self):
        if self.first is not None:
            current = self.first
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'LinkedList [{", ".join(values)}]'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self.__init__()

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None) 
        if self.first is None: 
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.limit += 1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node
        self.limit += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index == 0:
            self.push(value)
        elif index >= self.limit:
            self.add(value)
        else:
            current_node = self.first
            cur_idx = 0
            while cur_idx < index - 1:
                current_node = current_node.next
                cur_idx += 1
            prev_next = current_node.next
            current_node.next = Node(value, prev_next)
            self.limit += 1
        return

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, 
                если элемент не найден
        """
        current_node = self.first
        index = 0
        while current_node and current_node.value != value:
            current_node = current_node.next
            index += 1
        if not current_node:
            return '???'
        return index

    def len(self):
        return self.limit

    def __iter__(self):
        self.pointer = self.first
        return self

    def __next__(self):
        if not self.pointer:
            raise StopIteration
        to_return = self.pointer
        self.pointer = self.pointer.next
        return to_return

    def __getitem__(self, item):
        cur_idx = 0
        cur_node = self.first
        while cur_idx < item:
            cur_node = cur_node.next
            cur_idx += 1
        return cur_node

    def __setitem__(self, key, value):
        cur_idx = 0
        cur_node = self.first
        while cur_idx < key:
            cur_node = cur_node.next
            cur_idx += 1
        cur_node.value = value

    def __len__(self):
        return self.limit


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)

    L.insert('5656', 2)
    print("list = ", L)

    L.insert('54656', 3)
    print("list = ", L)

    print(L.find(2))
    print(L.find(22))

    print(L)
    print(L.first)

    # TODO: реализовать интерфейс итерации
    for el in L:
        print(el)
    # Напомню принцип работы итератора:
    iterator_L = iter(L)  # L.__iter__()
    print(next(iterator_L))  # it.__next__()

    # реализовать обращение по индексу и изменение значение по индексу
    print('l3', L[3])
    L[3] = "new"
    print('l3', L[3])

    # реализовать создание нового списка с задание начальных элементов
    L = LinkedList(2, 4, 6, -12)
    print(L)
