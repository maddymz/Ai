class ListNode:
    def __init__(self, data):
        self._data = data
        self._next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def removeDupesBuffer(self, llist):
        curr = llist.head
        prev = None
        store = {}
        while curr != None:
            if curr._data in store:
                prev._next = curr._next
            else:
                store[curr._data] = curr._data
                prev = curr
            curr = curr._next

        return llist

    def removeDupes(self, llist):
        cur = llist.head    
        while cur != None:
            runner = cur
            while runner._next != None:
                if runner._next._data == cur._data:
                    runner._next = runner._next._next
                else:
                    runner = runner._next
            cur = cur._next
        return llist

    def kthformlast(self, n, ll): # size of list is known 
        
        current = ll.head
        count = 0
        countEl = 0

        while current != None:
            current = current._next
            countEl += 1 
        f = countEl - n
        current = ll.head

        while current != None:
            count += 1
            current = current._next
            if count == f:
                element = current._data
        
        return element
    
    #size not known 
    def recursionKth(self, glist, k):
        if glist.head == None:
            return 0
        
        index = self.recursionKth(glist.head._next, k) + 1

        if index == k :
            return index, glist.head.data

    def deleteMiddleNode(self, node):
        if node == None or node._next == None:
            node._data = None
            return False
        
        n = node._next
        node._data = n._data
        node._next = n._next


        return True

    def printList(self):
        curr = self.head
        while curr:
            print(curr._data)
            curr = curr._next



if __name__ == "__main__":

    l = LinkedList()

    
    l.head = ListNode(4)
    second = ListNode(2)
    third = ListNode(3)
    f = ListNode(4)
    s = ListNode(2)

    l.head._next = second
    second._next = third
    third._next = f
    f._next = s

    node = l.head._next._next._next._next
    
    print(l.deleteMiddleNode(node))
    l.printList()


    
