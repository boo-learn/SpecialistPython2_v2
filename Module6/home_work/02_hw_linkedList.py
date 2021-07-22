# Для Связанного списка(LinkedList):
# 1. Реализуйте все задания в файле LinkedList.py Модуля-6
# 2. Реализуйте метод reverse() - меняющий значения всех нод(узлов) на противоположное.
# Значение первой ноды становится значением последней, значение второй, значением предпоследней.
# Примечание: при реализации не используйте список(list).
class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, nxt=None):
        self.value = value
        self.next = nxt

    def __str__(self):
        return f'Node: {self.value}'


class LinkedList:
    def __init__(self, *args, start=0):
        if len(args) == 0:
            self.first = None
            self.last = None
            self.__len = 0
        else:
            self.first = Node()
            current_node = self.first
            i = 0
            while True:
                current_node.value = args[i]
                if i == len(args) - 1:
                    break
                current_node.next = Node()
                current_node = current_node.next
                i += 1
            self.last = current_node
        self.start = start - 1  # инициализация счетчика

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
        self.__init__()

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тот же узел, т.к. он единственный
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
            # self.first и self.last будут указывать на один и тот же узел
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
        current_index = 0
        current = self.first
        while current.next is not None:
            if current_index == index - 1:
                break
            current = current.next
            current_index += 1

        prev_node = current
        next_node = prev_node.next
        new_node = Node(value, next_node)
        prev_node.next = new_node
        self.__len += 1

    def find(self, value):
        """
        Ищет элемент со значением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        current_node = self.first
        i = 0
        while current_node:
            if current_node.value == value:
                return i
            current_node = current_node.next
            i += 1
        return '????'

    def len(self):
        return self.__len

    def __len__(self):
        return self.len()

    def __setitem__(self, index, value):
        current_node = self.first
        i = 0
        while current_node:
            if i == index:
                current_node.value = value
            current_node = current_node.next
            i += 1
        return 'Index is out of range'

    def __getitem__(self, index):
        current_node = self.first
        i = 0
        while current_node:
            if i == index:
                return current_node.value
            current_node = current_node.next
            i += 1
        return 'Index is out of range'

    def __iter__(self):
        self.i = self.start  # сброс счетчика
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self):
            return self[self.i]
        else:
            raise StopIteration

    def reverse(self):
        rev_list = LinkedList()
        current_node = self.first
        while current_node:
            rev_list.push(current_node.value)
            current_node = current_node.next
        self.first = rev_list.first
        self.last = rev_list.last


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)
    print("Исходный список после добавления 3-х элементов (add) = ", L)
    L.push(0)
    print("Список после L.push(0) = ", L)
    L.insert(-9, 3)
    print("Список после L.insert(-9, 3) = ", L)
    # L.clear()
    print('Длина списка 1-ый вариант: ', L.len())
    print('Длина списка 2-ой вариант: ', len(L))
    print('Искомый элемент под индексом 2 = ', L.find(2))

    print("list = ", L)

    print('Работа интерфейса итерации с реализацией сброса счетчика')
    for el in L:
        print(el)

    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    print('Текущее значение по индексу [0]: ', L[0])
    L[0] = "new"
    print('Новое значение по индексу [0]: ', L[0])

    L = LinkedList(2, 4, 6, -12)
    print('Новый связанный список по начальным значениям: ', L)

    L.reverse()
    print('Реверс списка: ', L)
