
class DoublyLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next = b
b.prev = a
b.next = c
c.prev = b

print a.value