        def clear(self):
        """
        Очищаем список
        """
        self.first = None
        self.last = None
        #   raise TypeError("Not implemented")
        
        def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        # TODO: реализовать вставку
        if self.first is None:
            push(self, value)
        else:
            current = self.first
            cur_index = 0
            while cur_index < index:
                current = current.next
                cur_index += 1
            current_next = current.next
            new_node = Node(value, current_next)
            current.next = new_node
