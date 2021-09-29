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

        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        self.length = length

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out +=','+ str(current.value)
            return out + ']'

        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self.first=None
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
        self.length+=1

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
        self.length += 1

    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
         """
        self.length += 1
        if index==0:
            self.push(value)
            return
        if index==self.length:
            self.add()
            return
        current_node=self.first
        for _ in range(1,index):
            current_node=current_node.next
        new_node=Node(value,current_node.next)
        current_node.next=new_node
        return


    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        current_node=self.first
        i=0
        while value!=current_node.value:
            if current_node.next==None:
                raise IndexError("Значение не найдено")
            current_node=current_node.next
            i+=1
        return i
        #raise IndexError("Значение не найдено")

    # def len(self):
    #     # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
    #     length = 0
    #     if self.first is not None:
    #         current = self.first
    #         while current.next is not None:
    #             current = current.next
    #             length += 1
    #     return length + 1  # +1 для учета self.first


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(4)
    L.add(5)

    print("list = ", L)
    L.insert(6,3)
    print("list = ", L)
    print(L.find(6))
    print(L.length)




   
