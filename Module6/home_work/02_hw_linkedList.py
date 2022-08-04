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
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента +
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                out += ','
                current = current.next
                out += str(current.value)
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка +? что значит очистить список?
        if self.first is not None:
            current = self.first
            current.value = None
            #self.first = None
            #self.last = None
            while current.next is not None:
                current = current.next
                current.value = None

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
        # TODO: реализовать вставку +
        if self.first is not None:
            current_node = self.first
            new_node = Node(value, None)
            count = 0
            if index == 0:
                self.first = new_node
                new_node.next = current_node
                return
            else:
                while current_node:
                    if index - 1 == count:
                        new_node.next = current_node.next
                        current_node.next = new_node
                        return
                    count += 1
                    current_node = current_node.next
                print("Элемент добавить не удалось, список слишком короткий")

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента +-
        #   подумать над возвращаемым значением, если элемент со значение value не найден+
        count = 0
        out = ""
        if self.first is not None:
            current = self.first
            while current.next is not None:
                if current.value == value:
                    out += str(count) + " "
                count += 1
                current = current.next
            if out == "":
                return "???"
            return out


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

    L.insert(6, 2)
    L.insert(2, 3)
    print("list = ", L)

    fond_indx = L.find(6)
    print(fond_indx)
    L.clear()
    print("list = ", L)

    # TODO: реализовать интерфейс итерации
    # for el in L:
    #     print(el)
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
