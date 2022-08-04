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


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)
pred_node = None
# TODO: создайте цепочку нод из имен списка
for name in names:
    if pred_node is None:
      first = Node(name,None)
      pred_node = first
    else:
      pred_node = Node(name,pred_node)


# TODO: Передайте первую ноду в функцию print_nodes_value(), чтобы получить значения всех нод в цепочке

first_node = first
print_nodes_value(first_node)
