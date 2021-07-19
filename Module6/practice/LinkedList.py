class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"Node: {self.value}"


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.__len = 0
        if args:
            for agr in args:
                self.add(agr)

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ',' + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def __getitem__(self, idx):
        if type(idx) is not int:
            raise TypeError('LinkedList indices must be integers')
        if idx >= len(self) or abs(idx) > len(self):
            raise IndexError('LinkedList index out of range')

        idx = idx % len(self)
        cur_node = self.first
        while idx > 0:
            idx -= 1
            cur_node = cur_node.next
        return cur_node.value

    def __setitem__(self, idx, value):
        if type(idx) is not int:
            raise TypeError('LinkedList indices must be integers')
        if idx >= len(self) or abs(idx) > len(self):
            raise IndexError('LinkedList assignment index out of range')

        idx = idx % len(self)
        cur_node = self.first
        while idx > 0:
            idx -= 1
            cur_node = cur_node.next
        cur_node.value = value

    def __iter__(self):
        self.cur = -1
        return self

    def __next__(self):
        if self.cur < len(self) - 1:
            self.cur += 1
            return self[self.cur]
        else:
            raise StopIteration

    def clear(self):
        """
        Очищаем список
        """
        self.__init__()

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
        self.__len += 1

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
        self.__len += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index == 0:
            self.push(value)
            return
        if index >= self.len():
            self.add(value)
            return

        cur_idx = 0
        current = self.first
        while current.next is not None:
            if cur_idx == index - 1:
                break
            current = current.next
            cur_idx += 1

        prev_node = current
        next_node = current.next
        new_node = Node(value, next_node)
        prev_node.next = new_node
        self.__len += 1

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        idx = 0
        cur_node = self.first
        while cur_node:
            if cur_node.value == value:
                return idx
            else:
                idx += 1
                cur_node = cur_node.next
        raise ValueError(f"{value} is not in LinkedList")

    def len(self):
        return self.__len

    def __len__(self):
        return self.len()


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)
    L.insert(-4, 0)

    print("list = ", L)

    for el in L:
        print(el)

    print(L[0])
    L[0] = "new"
    print(L[0])

    L = LinkedList(2, 4, 6, -12)
    print(L)
