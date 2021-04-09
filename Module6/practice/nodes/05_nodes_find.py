class Node:
    """Класс для узла списка. Хранит значение и указатель на следующий узел."""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def len_nodes(start_node):
    """
    Возвращает целое число - кол-во нод у цепочке
    """
    count = 1
    node = start_node
    while node.next:
        count += 1
        node = node.next
    return count


def find_node_by_value(start_node, value):
    """
    Возвращает индекс ноды с заданным значением(value).
    Если нода с указанным значение(value) не найдена, дублируйте поведение методы .index() списка
    """
    list_len = len_nodes(start_node)
    index = 0
    while iter != list_len:
        start_node = start_node.next
        try:
            if start_node.value == value:
                print(f'{index=} {start_node.value=}')
                break
        except AttributeError:
            print('В списке нет такого элемента')
            break
        index += 1


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


if __name__ == '__main__':
    # Дан список из произвольного количества имен
    names = gen_names_list()
    print(names)

    # TODO: скопируйте цепочку нод из предыдущей задачи
    prev = None
    for name in names[::-1]:
        node = Node(value=name, next=prev)
        prev = node


    # TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
    #  напишите реализацию функции find_node_by_value()
    first_node = node
    value = "Линус"
    find_node_by_value(first_node, value)
