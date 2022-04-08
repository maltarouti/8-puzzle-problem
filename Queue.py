

class Queue:
    #a constructor 
    def __init__(self):
        self.elements = list()
        self.size = 0

    #a function that returns (true: if empty false otherwise).
    def is_empty(self):
        return len(self.elements) == 0

    #a function that inserts a node in the queue 
    def enqueue(self, node):
        self.elements.append(node)
        self.size += 1

    #returns the first element without removing it from the queue.
    def peek(self):
        return self.elements[0]

    #returning the first element and remove it from the queue.
    def pop(self):
        if not self.is_empty():
            temp = self.elements.pop(0)
            self.size -= 1
            return temp
        else:
            return None

