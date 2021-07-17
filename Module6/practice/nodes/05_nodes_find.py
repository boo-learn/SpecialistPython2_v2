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
    current_node = start_node
    i = 0
    while current_node:
        if current_node.value == value:
            return i
        current_node = current_node.next
        i += 1
    return 'Значение не найдено'


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

value = "Ирина"
print(f'Индекс искомого {value} : {find_node_by_value(first_node, value)}')
