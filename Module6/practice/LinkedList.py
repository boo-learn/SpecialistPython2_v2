# НЕДОДЕЛАННЫЙ find

    def find(self, value):
        """
      Ищет элемент со зачением value
      :param value: значение искомого элемента
      :return: индекс искомого элемента, или ???, если элемент не найден
      """

        current_node = self.first
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.value:
                results.append(node_id)
            current_node = current_node.next
            node_id = node_id + 1
        return results
        # # TODO: реализовать поиск элемента
        # #   подумать над возвращаемым значением, если элемент со значение value не найден
        # raise TypeError("Not implemented")
