import math as math

class StackNode:
    def __init__(self, data):
        self._data = data
        self._next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def peek(self):
        return self.head._data

    def push(self, item):
        node = StackNode(item)
        node._next = self.head
        self.head = node
    

    def pop(self):
        assert not self.isEmpty(), "Cannot pop if stack is empty"
        curr = self.head
        curr = curr._next
        self.head = curr


    def printStack(self):
        curr = self.head

        while curr != None:
            print(curr._data)
            curr = curr._next

class StackWithMin(Stack):
    def __init__(self):
        self.auxS = Stack()
        self.oldStack = Stack()

    def push(self, item):
        if self.isEmpty:
            self.oldStack.push(item)
            self.auxS.push(item)
        else:
            self.oldStack.push(item)
            y = self.auxS.pop()
            self.auxS.push(y)
            if item < y:
                self.auxS.push(item)
            else:
                self.push(y)

    def pop(self):
        value = self.oldStack.pop()
        self.auxS.pop()    
        return value
    
    def getMin(self):
        val = self.auxS.pop()
        self.auxS.push(val)
        return val

if __name__ == "__main__":

    # s = Stack()
    newS = StackWithMin()
    newS.push(2)
    newS.push(8)
    newS.push(5)
    newS.push(3)
    print(newS.getMin())
    newS.pop()
    newS.printStack()
