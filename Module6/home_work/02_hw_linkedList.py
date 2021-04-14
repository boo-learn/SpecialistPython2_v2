# Для Связанного списка(LinkedList) реализуйте метод reverse() - меняющий значения всех нод(узлов) на противоположное.
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
        self.first = None
        self.last = None
        self.length = 0
        self.current = None
        for arg in args:
            self.add(arg)

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
        if self.first is None:
            return
        current_node = self.first
        self.first.value = None
        while current_node.next is not None:
            next_node = current_node.next
            current_node.next = None
            current_node.value = None
            current_node = next_node
        self.first = None
        self.last = None
        self.length = 0
        self.current = None

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        self.length += 1
        new_node = Node(value, None)
        if self.first is None:
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = new_node
        else:
            # здесь, уже на разные
            self.last.next = new_node
            self.last = new_node

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        self.length += 1
        if self.first is None:
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index == 0:
            self.push(value)
            return
        if index > self.len():
            self.add(value)
            return
        self.length += 1
        prev_node = self.getnode(index - 1)
        new_node = Node(value, prev_node.next)
        prev_node.next = new_node

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или raise ValueError, если элемент не найден
        """
        current = self.first
        index = 0
        if current.value == value:
            return index
        while current and current.next is not None:
            current = current.next
            index += 1
            if current.value == value:
                return index
        raise ValueError(f"Элемент со значением {value} не найден")

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

    def getnode(self, index):
        if self.first is None:
            raise IndexError("...")
        current = self.first
        cur_index = 0
        if cur_index == index:
            return current
        while current.next is not None:
            current = current.next
            cur_index += 1
            if cur_index == index:
                return current
        raise IndexError("...")

    def __getitem__(self, index):
        return self.getnode(index).value

    def __setitem__(self, index, value):
        self.getnode(index).value = value

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        # length = 0
        # if self.first is not None:
        #     current = self.first
        #     while current.next is not None:
        #         current = current.next
        #         length += 1
        # return length + 1  # +1 для учета self.first
        return self.length

    def reverse(self):
        if self.last is None:
            return
        current_node = self.first
        next_node = current_node.next
        while next_node is not None:
            previous_node = current_node
            current_node = next_node
            next_node = current_node.next
            current_node.next = previous_node
        self.first.next = None
        self.first, self.last = self.last, self.first
