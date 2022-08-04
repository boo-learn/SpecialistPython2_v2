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
    num_nodes = 0
    while current_node:
        current_node = current_node.next
        num_nodes += 1
        if current_node.value == value:
            print (num_nodes)
            return
    print("No node with this value")


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
start_node = Node(names[0])
current_node = start_node
for name in names[1:]:
    node = Node(name)
    current_node.next = node
    current_node = node


# TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
#  напишите реализацию функции find_node_by_value()
first_node = start_node
value = "Екатерина"
find_node_by_value(first_node, value)
