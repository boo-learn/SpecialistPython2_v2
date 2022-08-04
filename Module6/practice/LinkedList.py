class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, *values):
        self.first = None
        self.last = None
        self.size = 0

        self.curr_elem = None

        for value in values:
            self.add(value)

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ',' + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        if self.first is not None:
            self.first = None
            self.size = 0
        return self.first

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
        self.size += 1

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
        if index > self.size:
            raise IndexError(f'Указанный индекс {index} превышает размер списка {self.size}')
        elif index == 0:
            self.push(value)
        else:
            new_node = Node(value)
            curr_index = 1
            prev_node = self.first

            while curr_index <= index:
                curr_node = prev_node.next
                if curr_index == index:
                    prev_node.next = new_node
                    new_node.next = curr_node
                prev_node = curr_node
                curr_index += 1
        self.size += 1

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        curr_node = self.first
        curr_index = 0
        while curr_node:
            if curr_node.value == value:
                return curr_index
            curr_node = curr_node.next
            curr_index += 1
        return f'Значение {value} не найдено'

    def len(self):
        return self.size

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current:
            iteration_val = self.current.value
            self.current = self.current.next
            return iteration_val
        else:
            raise StopIteration

    def get(self, index):
        i = 0
        if index >= self.size:
            raise IndexError
        current_node = self.first
        while current_node:
            if i == index:
                return current_node
            i += 1
            current_node = current_node.next

    def __getitem__(self, item):
        return self.get(item).value

    def __setitem__(self, item, value):
        self.get(item).value = value


'''
Блок проверок
'''
if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)
    print("list = ", L)
    L.insert(4, 1)
    print(L)
    print(L.find(4))
    print(L.len())
    L.clear()
    print(L)
    print(L.find(4))
    L = LinkedList(2, 4, 6, -12)
    print(L)
    for el in L:
        print(el)
    print(L[0])
    L[0] = "new"
    print(L[0])
