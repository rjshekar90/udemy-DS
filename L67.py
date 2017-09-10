
# Implementation of Stack class

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]       #returns the last item in the list.

    def size(self):
        return len(self.items)

s  = Stack()

s.push(100)
s.push(200)
s.push(500)

print s.peek()
