class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_nodes_value(start_node):
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]



# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: создайте цепочку нод из имен списка
node0 = Node("")
node1 = Node("")
node2 = Node("")
node3 = Node("")
node4 = Node("")
node5 = Node("")
node6 = Node("")
node7 = Node("")
node8 = Node("")
node9 = Node("")
...
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
# TODO: Передайте первую ноду в функцию print_nodes_value(), чтобы получить значения всех нод в цепочке
first_node = node0
print_nodes_value(first_node)
