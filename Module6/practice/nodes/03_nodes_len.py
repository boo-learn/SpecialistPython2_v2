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
    cnt = 0
    current_node = start_node
    while current_node:
        cnt += 1
        current_node = current_node.next
    print(cnt)


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: создайте цепочку нод из имен списка
node_start = Node(value=names[0])
node_prev = node_start
for name in names[1:]:
    node_next = Node(value=name)
    node_prev.next = node_next
    node_prev = node_next

# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
first_node = node_start
len_nodes(first_node)
