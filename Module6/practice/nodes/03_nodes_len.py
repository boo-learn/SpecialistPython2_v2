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
    """
    Возвращает целое число - кол-во нод у цепочке
    """
    current_node = start_node
    c = 0
    while current_node:
        current_node = current_node.next
        c += 1
    return c

# Дан список из произвольного количества имен
names = gen_names_list(10)
print(names)

current_node = None
first_node = None
for name in names:
    if current_node is None:
        current_node = Node(name)
        first_node = current_node
    else:
        current_node.next = Node(name)
        current_node = current_node.next

# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
print(len_nodes(first_node))
