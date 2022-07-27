class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def find_node_by_value(start_node, value):
    current_node = start_node
    idx = 0
    while current_node:
        if current_node.value == value:
            print(f"Index of value {value} is {idx}")
            exit()
        idx += 1
        current_node = current_node.next
    print(f"Value {value} is not found")


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
    counter = 0
    if not start_node is None:
        counter += 1

    while not start_node.next is None:
        counter += 1
        start_node = start_node.next

    return counter


def print_node_by_index(start_node, index):
    cur_index = 0

    while cur_index < index:
        start_node = start_node.next
        cur_index += 1

    print(f"Node with index {index} = {start_node.value}")


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

current_node = Node(names[0])
first_node = current_node
for name in names[1:]:
    next_node = Node(name)
    current_node.next = next_node
    current_node = next_node

# TODO: Передайте первую ноду в функцию print_nodes_value(), чтобы получить значения всех нод в цепочке


print_nodes_value(first_node)

# TODO: Передайте первую ноду в функцию len_nodes(), чтобы получить количество нод в цепочке

length = len_nodes(first_node)
print(f"length {length}")

# TODO: Передайте первую ноду и индекс ноды, значение которой нужно вывести, в функцию print_node_by_index()
#  напишите реализацию функции print_node_by_index()

index = length - 2

print_node_by_index(first_node, index)

# TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
#  напишите реализацию функции find_node_by_value()
value = 'Марина'
find_node_by_value(first_node, value)
