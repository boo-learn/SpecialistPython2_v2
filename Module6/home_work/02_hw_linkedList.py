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
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            return out[:-1] + ']'
        return 'LinkedList []'

    def clear(self):
        self.first = self.last = None

    def add(self, value):
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def push(self, value):
        if self.first is None:
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def insert(self, value, index):
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
        count = 0
        node = self.first
        while node:
            if node.value == value:
                return count
            count += 1
            node = node.next
        return -1

    def len(self):
        length = 0
        if self.first is not self.last:
            current = self.first
            while current.next is not self.last:
                current = current.next
                length += 1
        return length + 2  # +1 для учета self.first

    def reverse(self):
        _L_reversed = LinkedList()
        for node in self:
            _L_reversed.push(node.value)
        self.clear()
        for node in _L_reversed:
            self.add(node.value)
        del _L_reversed

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

    T_L = LinkedList(2, 4, 'new', 47)
    print(T_L)
    T_L.reverse()
    print(T_L)