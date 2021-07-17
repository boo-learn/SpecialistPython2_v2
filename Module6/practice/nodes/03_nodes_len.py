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
    count = 1
    while start_node.next:
        count += 1
        start_node = start_node.next
    return count


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

node_0 = Node(names[0])
cur_node = node_0
for name in names[1:]:
    cur_node.next = Node(name)
    cur_node = cur_node.next

first_node = node_0
print(len_nodes(first_node))
