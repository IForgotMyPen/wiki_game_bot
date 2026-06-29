class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        newNode = Node(self)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty!'
        else:
            temp = self.head
            self.head = self.head.next

            self.length -= 1

            return temp.data
    
    def peek(self):
        return self.head.data
    
    def isEmpty(self):
        return self.length == 0
    