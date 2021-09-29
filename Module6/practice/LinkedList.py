class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        self.__len = 0
    
    def __str__(self):
        return f"Node: {self.value}"


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value) + ','
            return out[:-1] + ']'
        return 'LinkedList []'

    def clear(self, value):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        # raise TypeError("Not implemented")
        self.__init__()
        
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
        #self.__len += 1

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
        self.__len += 1
        
    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        # TODO: реализовать вставку
        #raise TypeError("Not implemented")

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
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        # raise TypeError("Not implemented")
        self.value = value
        self.next = next
        #for i in range(len

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
#         length = 0
#         if self.first is not None:
#             current = self.first
#             while current.next is not None:
#                 current = current.next
#                 length += 1
#         return length + 1  # +1 для учета self.first
        self.len()


if __name__ == "__main__":

    L = LinkedList()
    print("empty list = ", L)
    L.clear(1)
    print("list = ", L)
    L.add(1)
    print("list = ", L)
    L.add(2)
    print("list = ", L)
    L.add(3)
    print("list = ", L)
    L.insert(-5, 1)
    print("list = ", L)
