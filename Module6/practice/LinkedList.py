class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# class NodeIterator:
#     def __init__(self, node):
#         self.node = node
# 
#     def __next__(self):
#         current_node = self.node
#         while current_node:
#             returned_node = current_node
#             current_node = current_node.next
#             return 

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента(solved)
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next:
                current = current.next
                if self.last == current:
                    out += str(current.value)
                    break
                out += str(current.value) + ','
            return out + ']'
        return 'LinkedList []'

    def __iter__(self):
        return NodeIterator(self)

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка (solved)
        self.first = None
        self.last = None

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = self.first = new_node
        else:
            self.last.next = self.last = new_node

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
        # TODO: реализовать вставку (solved)
        current_node = self.first
        next_index = 0
        if index == 0:
            self.push(value)
            return
        if index >= self.len():
            self.add(value)
            return
        while current_node:
            previous_node = current_node
            current_node = current_node.next
            next_index += 1
            if next_index == index:
                new_node = Node(value, current_node)
                previous_node.next = new_node
                break
        return

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        current_node = self.first
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            index += 1
            current_node = current_node.next
        return IndexError("Указанные значения не найдены")


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

L.add(4)
print("list = ", L)
L.insert(4, 2)
print("list = ", L)
print(L.find(4))

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
