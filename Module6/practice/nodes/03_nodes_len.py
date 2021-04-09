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
    prev_node = Node(names[-1])
    count = 0
    for name in names[::-1][1:]:
        next_node = Node(name, prev_node)
        prev_node = next_node
        count += 1
    return count



# Дан список из произвольного количества имен
names = gen_names_list()
print(names)
print(len_nodes(names))

#
...

first_node = Node('Василий')
len_nodes(first_node)
