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
    len = 0
    while current_node:
        len += 1
        current_node = current_node.next
    return len


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
first_node = Node(names[0])
current_node = first_node

for name in names[1:]:
    new_node = Node(name)
    current_node.next = new_node
    current_node = new_node




# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
print(len_nodes(first_node))
