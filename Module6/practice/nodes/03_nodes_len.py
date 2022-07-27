class Node:
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


def len_nodes(start_node):
    """
    Возвращает целое число - кол-во нод у цепочке
    """
    result = 0
    curr_node = start_node
    while curr_node:
        curr_node = curr_node.next
        result += 1

    print(result)


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
first_node = Node(names[0])
prev_node = first_node
for nm in names[1:]:
    new_node = Node(nm)
    if prev_node:
        prev_node.next = new_node
        prev_node = new_node

# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
len_nodes(first_node)
