class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

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
    count =1
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next
        count += 1
    return count


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
names = gen_names_list()
print(names)

# TODO: создайте цепочку нод из имен списка
# node1 = Node(names[0])
current_node = None
first_node = None
for name in names:
    if current_node is None:
        current_node = Node(name)
        first_node = current_node
    else:
        current_node.next = Node(name)
        current_node = current_node.next


# TODO: Передайте первую ноду в функцию print_nodes_value(), чтобы получить значения всех нод в цепочке
print_nodes_value(first_node)

# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке
num = len_nodes(first_node)
print(f"{num=}")
