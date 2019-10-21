class ArrayStack:
    def __init__(self):
        self.arr = []
    

    def length(self):
        if self.arr == None or len(self.arr) == None:
            return False
        else:
            return len(self.arr)

    def push(self, item):
        self.arr.append(item)
    
    def pop(self):
        if self.arr != None or len(self.arr) != None:
            l = self.length()
            item = self.arr.remove(self.arr[l-1])

        return item

    def print(self):
        for i in range(self.length()):
            print(self.arr[(self.length()-1) - i])



if __name__ == "__main__":

    s = ArrayStack()

    s.push(2)
    s.push(7)
    s.push(67)
    s.push(23)

    s.pop()
    s.print()