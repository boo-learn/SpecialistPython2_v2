class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'Node:{self.value}, next:{self.next}'


# Создаем ноды(узлы)
node0 = Node("Иван")
node1 = Node("Алекс")
node2 = Node("Петр")
node3 = Node("Анна")

# TODO: Добавьте еще несколько нод с именами
node4 = Node("Кевин")
node5 = Node("Поль")
node6 = Node("Рэнуа")
node7 = Node("Семён")
node8 = Node("Колян")

# Связываем ноды
node0.next = node1
node1.next = node2
node2.next = node3

# TODO: Свяжите добавленные выше ноды вместе
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

# Пройдемся по значениям всех нод, начиная с первой
current_node = node0
while current_node:
    print(current_node.value)
    current_node = current_node.next
