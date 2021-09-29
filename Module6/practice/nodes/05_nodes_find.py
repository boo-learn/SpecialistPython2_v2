class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"Node:{self.value}, next:{self.next}"

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
        i+=1
        current_node = current_node.next
    print("нет значения")


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

# TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
#  напишите реализацию функции find_node_by_value()

value = "Линус"
print(find_node_by_value(first_node, value))
