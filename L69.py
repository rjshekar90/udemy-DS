
#Implementation of Queue class

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue(100)
q.enqueue(200)

print q.dequeue()