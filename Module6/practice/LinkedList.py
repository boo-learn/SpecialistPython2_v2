class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __repr__(self):
        # убрать вывод запятой после последнего элемента
        if self.first:
            current = self.first
            out = '[' + str(current.value)
            while current.next:
                current = current.next
                out += ', ' + str(current.value)
            return out + ']'
        return '[]'

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        self.first = None
        self.last = None

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
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
            self.last = self.first = Node(value)
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if self.first is None:
            self.first = self.last = Node(value)
            return

        if not index:
            self.push(value)
            return

        count = 0
        current = self.first
        while current:
            if index - 1 == count:
                new_node = Node(value, current.next)
                current.next = new_node
                return
            current = current.next
            count += 1

        raise IndexError('list index out of range')

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        count = 0
        current_node = self.first
        while current_node:
            if current_node.value == value:
                return count
            current_node = current_node.next
            count += 1

        raise ValueError(f'{value} is not in LinkedList')

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        count = 0
        if self.first:
            current = self.first
            while current:
                current = current.next
                count += 1

            return count
        return count


if __name__ == "__main__":
    ll = LinkedList()
    print("list =", ll)

    ll.add(1)
    ll.add(2)
    ll.add(3)
    print("list =", ll)

    ll.push(1)
    ll.push(2)
    ll.push(3)
    print("list =", ll)

    ll.insert(5, 3)
    print("list =", ll)

    print("len(list) =", ll.len())

    print("find(5) = ", ll.find(5))
