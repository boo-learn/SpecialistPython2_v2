# Для Связанного списка(LinkedList):
# 1. Реализуйте все задания в файле LinkedList.py Модуля-6
# 2. Реализуйте метод reverse() - меняющий значения всех нод(узлов) на противоположное.
# Значение первой ноды становится значением последней, значение второй, значением предпоследней.
# Примечание: при реализации не используйте список(list).

class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

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
        self.i = 0

        if args is not None:
            for el in args:
                self.add(el)

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента

        s = ','.join(str(el) for el in self)  # We created iterator for LinkedList
        return 'LinkedList [' + s + ']'

        # if self.first is not None:
        #     current = self.first
        #     out = 'LinkedList [' + str(current.value) + ','
        #     while current.next is not None:
        #         current = current.next
        #         out += str(current.value)
        #         if current.next is not None:
        #             out += ','
        #     return out + ']'
        # return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        if self.first is not None and self.first is not self.last:
            current = self.first
            next_node = current.next

            while next_node is not None:
                current = None
                current = next_node
                next_node = current.next

        current = None
        next_node = None
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
        if index > 0 and index > self.size:
            print(f"Невозможно вставить элемент в позцию {index} т.к. размер списка {self.size}")
            return

        if index == 0:
            self.push((value))
            return

        current = self.first
        idx = 0
        while current is not None:
            # print(f"idx = {idx} index={index}")
            if idx == index - 1:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node

                if index == 0:
                    self.first == new_node

                if index == self.size:
                    self.last = new_node

                self.size += 1

                return
            idx += 1
            current = current.next

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        idx = 0;
        if self.first is not None:
            current = self.first
            while current is not None:
                if current.value == value:
                    return idx
                current = current.next
                idx += 1

        return None

    def find_by_index(self, index):
        if self.size - 1 < index:
            raise IndexError(f"Нельзя обраится к элементу с индексом {index} т.к. размер списка {self.size}")

        current = self.first;
        idx = 0

        while current is not None:
            if idx == index:
                return current
            current = current.next
            idx += 1;

        raise IndexError(f"Элемент с индексом {index} не найден")

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.size:
            # print(f"self.i = {self.i} self.size={self.size}")
            self.i += 1;
            return self.find_by_index(self.i - 1)
        raise StopIteration

    def len(self):
        return self.size
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго

    def __getitem__(self, key):
        return self.find_by_index(key)

    def __setitem__(self, key, value):
        el = self.find_by_index(key)
        el.value = value

    def reverse(self):
        for idx in range(self.size - 1, 0, -1):
            if idx == 0:
                self[idx].next = None
            else:
                self[idx].next = self[idx - 1]

        self.first, self.last = self.last, self.first


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)
    L.insert(4, 3)
    L.insert(0, 0)
    L.insert('x', 4)
    # L.clear()
    print("list = ", L)

    print(f"Last element = {L.last.value}")
    print(f"First element = {L.first.value}")

    print(f"Index of  4 is {L.find(4)}")
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
    print(f"Значение нулевого элемента {L[0]}")
    L[0] = "new"
    print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    L = LinkedList(2, 4, 6, -12)
    print(L)

    L.reverse()
    print("Reversed ", L)
