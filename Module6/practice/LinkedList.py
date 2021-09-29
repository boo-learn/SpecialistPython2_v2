    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                if current.next is None:
                    out += str(current.value)
                else:
                    out += str(current.value) + ','
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        """
        Очищаем список
        """
        self.first = None
        self.last = None
