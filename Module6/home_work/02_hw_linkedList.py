# Для Связанного списка(LinkedList) реализуйте метод reverse() - меняющий значения всех нод(узлов) на противоположное.
# Значение первой ноды становится значением последней, значение второй, значением предпоследней.
# Примечание: при реализации не используйте список(list).
#!/usr/bin

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
        self.length = 0
        self.index = 0

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first == None:
            return 'LinkedList []'
        else:
            pointer = self.first
            if pointer.next != None:
                list_string = f'LinkedList [{str(pointer.value)}, '
            else:
                list_string = f'LinkedList [{str(pointer.value)}'
            while pointer.next != None:
                pointer = pointer.next
                if pointer.next != None:
                    list_string += f"{str(pointer.value)}, "
                else:
                    list_string += f"{str(pointer.value)}"
            return f"{list_string}]"

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        if self.first != None:
            pointer = self.first
            while pointer.next != None:
                pointer.value = 0
                self.first = pointer.next
                pointer = pointer.next
            pointer.value = 0
            self.first = None
            self.last = None
        self.length = 0

    def add(self, value):
        node = Node(value, None)
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.last == None:
            node = Node(value, None)
            self.first = node
            self.last = node
        else:
            node = Node(value, self.first)
            self.first = node
        self.length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if index == 0:
            self.push(value)
        elif index == self.length or index > self.length:
            self.add(value)
        else:
            pointer = self.first
            counter = 0
            while True:
                if counter == index - 1:
                    break
                pointer = pointer.next
                counter += 1
            node = Node(value, pointer.next)
            pointer.next = node
            self.length += 1

    def raise_error(self, value):
        raise ValueError(f"Элемент со значением {value} не найден")

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или raise ValueError, если элемент не найден
        """
        if self.first == None:
            self.raise_error(value)
        else:
            pointer = self.first
            counter = 0
            while pointer.next != None:
                if pointer.value == value:
                    return counter
                pointer = pointer.next
                counter += 1
            if pointer.value == value:
                return counter
            self.raise_error(value)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.first == None or self.next == None:
            raise StopIteration
        else:
            value = self.next.value
            self.index += 1
            return value

    def __getitem__(self, index):
        if index < self.length:
            pointer = self.first
            counter = 0
            while True:
                if counter == index:
                    break
                pointer = pointer.next
                counter += 1
            return pointer.value
        raise IndexError

    def __setitem__(self, index, value):
        if index < self.length:
            pointer = self.first
            counter = 0
            while True:
                if counter == index:
                    break
                pointer = pointer.next
                counter += 1
            pointer.value = value
        else:
            raise IndexError

    def reverse(self):
        half = self.length // 2
        for i in range(half):
            buf_first = self.__getitem__(i)
            buf_last = self.__getitem__(self.length - i - 1)
            self.__setitem__(i, buf_last)
            self.__setitem__(self.length - i - 1, buf_first)

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        return self.length

lst = LinkedList()
lst.reverse()
print(str(lst))
