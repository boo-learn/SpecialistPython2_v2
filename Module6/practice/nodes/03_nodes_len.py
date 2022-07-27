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
        counter = 0
        if not start_node is None:
           counter+=1

        while not start_node.next is None:
            counter += 1
            start_node = start_node.next

        return counter


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
