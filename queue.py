class LinkedNode:
    """A linked node to be used for linked list implementations.
    
    Attributes:
        data: The data being held by the node.
        next: A pointer to the next node in the linked list.
        """
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """A queue to be used for a breadth-first traversal.
    
    This queue implements a linked list.
    
    Attributes:
        head: The node at the beginning of the queue (i.e. the next node to be dequeued).
        tail: The node at the end of the queue.
        length: The total number of nodes in the queue."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        """Creates a new node and places it at the end of the queue.
        
        Keyword arguments:
            data: The data to be put in the new node.
        """
        newNode = LinkedNode(data)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
    
    def dequeue(self):
        """Returns the data stored in the node at the front of the queue and removes it from the
           queue."""
        if self.isEmpty():
            return 'Queue is empty!'
        else:
            temp = self.head
            self.head = self.head.next

            self.length -= 1

            return temp.data
    
    def peek(self):
        """Returns the data stored in the node at the front of the queue without removing it from 
           the queue."""
        return self.head.data
    
    def isEmpty(self):
        """Returns the length of the queue."""
        return self.length == 0
    