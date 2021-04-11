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
        self._length = 0
        self.first = None
        self.last = None
        self.marker = self.first
        if args:
            for arg in args:
                self.add(arg)

    def __repr__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ', ' + str(current.value)
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self._length = 0
        self.first = None
        self.last = None

        # TODO: реализовать очистку списка
        # raise TypeError("Not implemented")

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node
            self._length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self._length += 1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
            self._length += 1
        else:
            new_node = Node(value, self.first)
            self.first = new_node
            self._length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index >= self._length:
            self.add(value)
            return
        count = 0
        current_node = self.first
        previous_node = None
        while current_node:
            if count == index:
                node_to_insert = Node(value, current_node)
                if previous_node:
                    previous_node.next = node_to_insert
                    self._length += 1
                else:
                    self.first = node_to_insert
                    self._length += 1
                return
            count += 1
            previous_node = current_node
            current_node = current_node.next

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        count = 0
        cur_node = self.first
        while cur_node.value != value:
            if not cur_node.next:
                raise ValueError(f"'{value}' not in Linked list")
            cur_node = cur_node.next
            count += 1
        return count

    def __len__(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        # length = 0
        # if self.first is not None:
        #     current = self.first
        #     while current.next is not None:
        #         current = current.next
        #         length += 1
        return self._length  # +1 для учета self.first

    def __iter__(self):
        self.marker = self.first
        return self

    def __next__(self):
        if not self.marker:
            raise StopIteration
        node_to_return = self.marker.value
        self.marker = self.marker.next
        return node_to_return

    def __getitem__(self, index):
        count = 0
        current_node = self.first
        while current_node:
            if count == index:
                return current_node.value
            count += 1
            current_node = current_node.next
        raise IndexError('Node index out of range')

    def __setitem__(self, index, value):
        count = 0
        current_node = self.first
        while current_node:
            if count == index:
                current_node.value = value
                return
            count += 1
            current_node = current_node.next
        raise IndexError('Node index out of range')

    def __contains__(self, value):
        cur_node = self.first
        while cur_node.value != value:
            if not cur_node.next:
                return False
            cur_node = cur_node.next
        return True

    def __delitem__(self, index):
        if index >= self._length:
            raise IndexError('Node index out of range')
        count = 0
        current_node = self.first
        previous_node = None
        while current_node:
            if count == index:
                if previous_node:
                    previous_node.next = current_node.next
                    self._length -= 1
                else:
                    self.first = current_node.next
                    self._length -= 1
                return
            count += 1
            previous_node = current_node
            current_node = current_node.next

    def remove(self, value):
        count = 0
        cur_node = self.first
        previous_node = None
        while cur_node.value != value:
            if not cur_node.next:
                raise ValueError(f"'{value}' not in Linked list")
            previous_node = cur_node
            cur_node = cur_node.next
            count += 1
        if previous_node:
            previous_node.next = cur_node.next
            self._length -= 1
        else:
            self.first = cur_node.next
            self._length -= 1

    def reverse(self):
        offset = 1
        for i in range(self._length // 2):
            self[i], self[self._length - offset] = self[self._length - offset], self[i]
            offset += 1
        return self

    def __reversed__(self):
        self.marker = self.first
        return self.reverse()

    def pop(self, index=None):
        index = self._length - 1 if index == None else index
        count = 0
        current_node = self.first
        previous_node = None
        while current_node:
            if count == index:
                if previous_node:
                    previous_node.next = current_node.next
                    self._length -= 1
                    return current_node.value
                else:
                    self.first = current_node.next
                    self._length -= 1
                    return current_node.value
            count += 1
            previous_node = current_node
            current_node = current_node.next
        raise IndexError('Node index out of range')


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)
    print("list = ", L)
    
