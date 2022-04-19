    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + ','
            while current.next is not None:
                current = current.next
                out += str(current.value)
                if current.next is None:
                    break
                out += ','
            return out + ']'
        return 'LinkedList []'
