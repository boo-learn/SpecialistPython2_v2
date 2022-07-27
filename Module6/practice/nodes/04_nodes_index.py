class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_node_by_index(start_node, index):
    current_node = start_node
    count = 0
    while current_node:
        if index == count:
            print(current_node.value)
            return
        count += 1
        current_node = current_node.next

    raise IndexError(f"Нода с индексом {index} не найдена")


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

current_node = Node(names[0])
first_node = current_node
for name in names[1:]:
    next_node = Node(name)
    current_node.next = next_node
    current_node = next_node
index = 2
print_node_by_index(first_node, index)
