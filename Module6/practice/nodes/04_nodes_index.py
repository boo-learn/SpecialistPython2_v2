class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def print_nodes_value(start_node):
    current_node = start_node
    while current_node:
        print(current_node.value)
        current_node = current_node.next


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


def len_nodes(start_node):
    """
    Возвращает целое число - кол-во нод у цепочке
    """
    result = 0
    curr_node = start_node
    while curr_node:
        curr_node = curr_node.next
        result += 1

    return result


def print_node_by_index(start_node, index):
    """
    Выводит в терминал значение(value) ноды с заданным индексом(index). Индексация начинается с нуля.
    Если index = 0, выводим значение ноды start_node
    Считаем, что index гарантированно > 0
    """
    curr_index = 0
    curr_node = start_node
    list_length = len_nodes(start_node)

    if index >= list_length:
        print("Запрашиваемый индекс превышает размер списка")
        return

    while curr_node:
        if curr_index == index:
            print(curr_node.value)
            return
        curr_index += 1
        curr_node = curr_node.next


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
first_node = Node(names[0])
prev_node = first_node
for nm in names[1:]:
    new_node = Node(nm)
    if prev_node:
        prev_node.next = new_node
        prev_node = new_node

# TODO: Передайте первую ноду и индекс ноды, значение которой нужно вывести, в функцию print_node_by_index()
#  напишите реализацию функции print_node_by_index()
index = 3
print_node_by_index(first_node, index)
