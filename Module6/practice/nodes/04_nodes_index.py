class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_node_by_index(start_node, index):
    """
    Выводит в терминал значение(value) ноды с заданным индексом(index). Индексация начинается с нуля.
    Если index = 0, выводим значение ноды start_node
    Считаем, что index гарантированно > 0
    """
    count = 0
    while count < index:
        if start_node.next is not None:
            count += 1
            start_node = start_node.next
        else:
            raise IndexError(f"Element with index {index} do not exist")
    print(start_node.value)


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

node_0 = Node(names[0])
cur_node = node_0
for name in names[1:]:
    cur_node.next = Node(name)
    cur_node = cur_node.next

first_node = node_0
index = 7
print_node_by_index(first_node, index)

