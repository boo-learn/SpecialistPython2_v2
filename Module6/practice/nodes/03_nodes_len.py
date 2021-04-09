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
    len_node = 1
    while start_node.next != None:
        start_node = start_node.next
        len_node += 1
    return  len_node


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

curr = None
for name in names[::-1]:
    curr = Node(name,curr)


print(len_nodes(curr))
