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
    i=0
    current_node = start_node
    while current_node:
        if i == index:
            print(current_node.value)
        current_node = current_node.next
        i+=1


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


# TODO: Передайте первую ноду и индекс ноды, значение которой нужно вывести, в функцию print_node_by_index()
#  напишите реализацию функции print_node_by_index()

index = 2
print_node_by_index(first_node, index)
print_node_by_index(first_node, index)
