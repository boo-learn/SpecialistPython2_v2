class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"Node:{self.value}, next:{self.next}"



def print_node_by_index(start_node, index):
    i = 0
    current_node = start_node
    while current_node:
        if index == i:
            return current_node.value
        i+=1
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



first_node = Node(names[0])
prev_node = first_node
for name in names[1:]:
    next_node = Node(name)
    prev_node.next = next_node
    prev_node = next_node


# TODO: Передайте первую ноду и индекс ноды, значение которой нужно вывести, в функцию print_node_by_index()
#  напишите реализацию функции print_node_by_index()
index = 0
print(print_node_by_index(first_node, index))
