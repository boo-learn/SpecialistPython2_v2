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
    index = 0
    while current_node and current_node.value != value:
        current_node = current_node.next
        index += 1
    if not current_node:
        raise ValueError(f'{value} not in list')
    return index


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

# TODO: скопируйте цепочку нод из предыдущей задачи
current_node = None
for name in names:
    if not current_node:
        current_node = Node(name)
        first_node = current_node
    else:
        current_node.next = Node(name)
        current_node = current_node.next


# TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
#  напишите реализацию функции find_node_by_value()
value = 'Игнат'
print(find_node_by_value(first_node, value))
