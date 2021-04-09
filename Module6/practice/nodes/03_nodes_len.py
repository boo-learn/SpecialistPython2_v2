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
    len_count = 0
    current_node = start_node
    while current_node:
        len_count += 1
        current_node = current_node.next

    return len_count


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
prev_node = Node(names[-1])
for name in names[::-1][1:]:
    node = Node(name, prev_node)
    prev_node = node

# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
first_node = prev_node
print(len_nodes(first_node))
