class SumLists:
    def __init__(self):
        pass

    def add(self, l1, l2, carry):
        if l1 == None and l2 ==None and carry == None:
            return None
        
        result = ListNode()

        carry = carry

        if l1 != None:
            carry += l1.data
        if l2 != None:
            carry += l2.data
        
        result.data = (carry) % 2

        #recurse

        if l1 != None or l2 != None:
            more = ListNode()

            if l1 == None and l2 == None:
                more = slef.add(None)

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
