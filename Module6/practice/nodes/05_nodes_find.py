class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def find_node_by_value(start_node, value):
    """
    Возвращает индекс ноды с заданным значением(value).
    Если нода с указанным значение(value) не найдена, дублируйте поведение методы .index() списка
    """
    idx = 0
    while start_node:
        if start_node.value == value:
            return idx
        else:
            idx += 1
            start_node = start_node.next
    raise ValueError(f"{value} is not in list")


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
value = "Василий"
print(find_node_by_value(first_node, value))
