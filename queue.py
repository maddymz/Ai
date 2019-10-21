class QueueNode:
    def __init__(self, data):
        self._data = data
        self._next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def peek(self):
        return self.head._data

    def enqueue(self, item):
        node = QueueNode(item)
        if self.tail == None:
            self.head = node
            self.tail = node
            return
        self.tail._next = node
        self.tail = node
    
    def dequeue(self):
        assert not self.isEmpty(), "Cannnot dequeue form an empty Queue"
        curr = self.head
        self.head = curr._next

        if self.head == None:
            self.tail = None

        return curr._data
    
    def printQueue(self):
        curr = self.head
        while curr != None:
            print(curr._data)
            curr = curr._next

if __name__ == "__main__":

    q = Queue()

    q.enqueue(89)
    q.enqueue(67)
    q.enqueue(2)
    q.enqueue(4)

    # q.dequeue()
    print(q.peek())
    q.printQueue()


