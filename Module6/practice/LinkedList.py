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
        self.size = 0
        if len(args) > 0:
            for arg in args:
                self.add(value=arg)

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = f'LinkedList({self.size}) [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            return out[:-1] + ']'
        return f'LinkedList({self.size}) []'

    def clear(self):
        """
        Очищаем список
        """
        self.size = 0
        self.first = None
        self.last = None

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
        if index == 0:
            self.push(value, index)
        elif index >= self.size:
            self.add(value, index)
        else:
            prev_node = self.get(index - 1)
            new_node = Node(value=value, next=self.get(index))
            prev_node.next = new_node
            self.size += 1

    def get(self, index):
        """
        Ищет элемент по индексу
        :param index:
        :return:
        """
        if index >= self.size:
            raise IndexError(f"Нода с индексом {index} не найдена")
        cnt = 0
        current_node = self.first
        while current_node:
            if cnt == index:
                return current_node
                break
            cnt += 1
            current_node = current_node.next

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        current_node = self.first
        count = 0
        while current_node:
            if current_node.value == value:
                return count
            count += 1
            current_node = current_node.next
        raise LookupError(f"Нода со значением {value} не найдена")

    def len(self):
        return self.size

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is not None:
            temp = self.current.value
            self.current = self.current.next
            return temp
        else:
            raise StopIteration

    def __getitem__(self, i):
        return self.get(i).value

    def __setitem__(self, i, value):
        self.get(i).value = value


if __name__ == "__main__":
    L = LinkedList()
    print("empty list =", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list =", L)

    L.insert(4, 2)
    print("insert(4, 2) list =", L)

    L.push(5)
    print("push(5) list =", L)

    print("find(4) find =", L.find(4))

    print("Iteration list:", end=' ')
    for el in L:
        print(el, end=' ')
    print()

    print("get by index:", L[0])
    L[0] = "new"
    print("set by index:", L)

    L1 = LinkedList(2, 4, 6, -12)
    print('LinkedList(2, 4, 6, -12)', L1)

    L.clear()
    print("clear() list = ", L)
