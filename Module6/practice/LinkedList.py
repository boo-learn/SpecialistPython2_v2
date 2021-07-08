class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next_node=None, index=None):
        self.value = value
        self.next = next_node
        self.index = index

    def __str__(self):
        return f'<node> val={self.value}, id={self.index}'


class LinkedList:
    def __init__(self, *args):
        self.first = None
        self.last = None
        for val in args:
            self.add(val)

    def __str__(self):
        if self.first is not None:
            out = '[ '
            for node in self:
                out += f'{node} | '
            return out[:-3] + ' ]'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        self.first = self.last = None

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value=value)
        if self.first is None:
            self.last = new_node
            self.first = new_node
            new_node.index = 0
        else:
            new_node.index = self.last.index + 1
            self.last.next = new_node
            self.last = new_node

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:
            self.last = self.first = Node(value, None)
            self.first.index = 0
        else:
            new_node = Node(value, self.first)
            self.first = new_node
            self.first.index = 0
            current = self.first
            i = 1
            while current.next is not None:
                current = current.next
                current.index = i
                i += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if self.first is None or self.first.index == index:
            self.push(value)
        else:
            current = self.first
            while current.next is not None:
                current = current.next
                if current.index == index - 1:
                    tmp_node = current.next
                    current.next = Node(value=value, next_node=tmp_node, index=index)
                    current = current.next
                    while current.next is not None:
                        current = current.next
                        current.index += 1
                    break

    def find(self, value=None, index=None):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :param index: индекс узла списка
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        if index is None:
            for node in self:
                if node.value == value:
                    return node
            return None
        else:
            current = self.first
            if current.index == index:
                return current
            while current.next is not None:
                current = current.next
                if current.index == index:
                    return current
            return None

    def len(self):
        """
        возврат длины списка
        т.к. имеетсяи ндекс который постоянно считается на базе количества елементов
         достаточно вернуть его полс + 1
        :return:
        """
        return self.last.index + 1

    def __iter__(self):
        self.index_node = -1
        return self

    def __next__(self):
        self.index_node += 1
        current = self.find(index=self.index_node)
        if current is not None:
            return current
        else:
            raise StopIteration

    def __getitem__(self, index):
        current = self.find(index=index)
        return current.value

    def __setitem__(self, index, value):
        current = self.find(index=index)
        current.value = value

    def _update_index(self):
        i = 1
        current = self.first
        current.index = 0
        while current.next is not None:
            current = current.next
            current.index = i
            i += 1

    def del_item(self, value=None, index=None):
        if index is None:
            current = self.first
            if current.value == value:
                self.first = self.first.next
                self._update_index()
            else:
                for node in self:
                    if node.next.value == value:
                        print(node.next.next)
                        tmp_node = node.next.next
                        node.next = tmp_node
                        self._update_index()
                        print(self)
                        break
                else:
                    raise ValueError('не найдена Node')
        else:
            if self.first.index == index:
                self.first = self.first.next
                self._update_index()
            else:
                for node in self:
                    if node.index == index - 1:
                        node.next = node.next.next
                        self._update_index()
                        break


if __name__ == "__main__":
    L = LinkedList()
    # print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print(L)
    L.insert(5, 0)
    print(L)
    # TODO: реализовать интерфейс итерации
    for el in L:
        print(el)
    # TODO: реализовать обращение по индексу и изменение значение по индексу
    print(L[0])
    L[0] = "new"
    print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    L = LinkedList(2, 4, 6, -12)
    print(L)
    L.del_item(2)
    print(L)
    L.del_item(4)
    print(L)
    L.del_item(index=1)
    print(L)
