class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


def len_nodes(start_node):
    length = 0
    current_node = start_node
    while current_node:
        length += 1
        current_node = current_node.next
    return length


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
node1 = Node(names[0])
current_node = node1
for name in names[1:]:
    current_node.next = Node(name)
    current_node = current_node.next


# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
print(len_nodes(node1))
