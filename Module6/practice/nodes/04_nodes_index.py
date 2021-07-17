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
    current_node = start_node
    c = 0
    while current_node:
        if c == index:
            return current_node.value
        current_node = current_node.next
        c += 1
    return 'Индекс находится за пределами списка'


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


# Дан список из произвольного количества имен
names = gen_names_list(10)
print(names)

current_node = None
first_node = None
for name in names:
    if current_node is None:
        current_node = Node(name)
        first_node = current_node
    else:
        current_node.next = Node(name)
        current_node = current_node.next

index = 5
print(print_node_by_index(first_node, index))
