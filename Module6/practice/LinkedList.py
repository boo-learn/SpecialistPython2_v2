class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        self.size = 0

        self.curr_elem = None

        for arg in args:
            self.add(arg)

    def __str__(self):
        if self.first is not None:
            current = self.first
            result = []
            while current is not None:
                result.append(str(current))
                current = current.next

            return f'LinkedList [{",".join(result)}]'

        return 'LinkedList []'

    def __getitem__(self, index):
        if index > self.size - 1:
            raise IndexError(f"Указанный индекс {index} превышает размер списка")
        if index < 0:
            raise ValueError(f"Указанный индекс {index} меньше 0")

        curr_node = self.first
        curr_index = 0

        while curr_node:
            if curr_index == index:
                return curr_node

            curr_node = curr_node.next
            curr_index += 1

        return None

    def __setitem__(self, index, value):
        change_node = self[index]
        change_node.value = value

    def __iter__(self):
        self.curr_elem = self.first
        return self

    def __next__(self):
        if self.curr_elem is None:
            raise StopIteration
        else:
            result = self.curr_elem
            self.curr_elem = self.curr_elem.next
            return result

    def clear(self):
        """
        Очищаем список
        """
        self.first = None
        self.last = None
        self.size = 0

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

        self.size += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index < 0:
            raise ValueError(f"Указанный индекс {index} меньше 0")
        if index >= self.size:
            raise IndexError(f"Указанный индекс {index} превышает размер списка {self.size}")

        if index == 0:
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
        :return: индекс искомого элемента, или -1, если элемент не найден
        """
        curr_node = self.first
        curr_index = 0

        while curr_node:
            if curr_node.value == value:
                return curr_index

            curr_node = curr_node.next
            curr_index += 1

        return -1

    def len(self):
        return self.size


L = LinkedList()
print("empty list = ", L)
L.add(1)
L.add(2)
L.add(3)

print("list = ", L)

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
print(L[0])
L[0] = "new"
print(L[0])

# TODO: реализовать создание нового списка с задание начальных элементов
L = LinkedList(2, 4, 6, -12)
print(L)
