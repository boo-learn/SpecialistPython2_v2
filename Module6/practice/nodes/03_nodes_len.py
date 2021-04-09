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
    count = 1
    node = start_node
    while node.next:
        count += 1
        node = node.next
    return count


if __name__ == '__main__':
    # Дан список из произвольного количества имен
    names = gen_names_list()
    print(names)

    # TODO: скопируйте цепочку нод из предыдущей задачи
    prev = None
    for name in names:
        node = Node(value=name, next=prev)
        prev = node

    # TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
    first_node = node
    nodes_len = len_nodes(first_node)
    print(nodes_len)
