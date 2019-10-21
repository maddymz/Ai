class SquareArray:
    def __init__(self):
        pass

    def sortedSquares(self, Array):
        for i in range(len(Array)):
            square = Array[i]*Array[i]
            Array[i] = square

            self.mergeSort(Array, [], 0, len(Array)-1)
        
        return Array

    
    def mergeSort(self, Array, helper, low, high):
        if low < high:
            middle = (low + high)//2
            self.mergeSort(Array, helper, low, middle)
            self.mergeSort(Array, helper, middle+1, high)
            self.merge(Array, helper, low, middle, high)

    def merge(self, Array, helper, low, middle, high):
        i = low
        for i in range(high):
            helper[i] = Array[i]

        hleft = low
        hright = middle + 1
        curr = low

        while hleft < middle and hright <= high:
            if helper[hleft] <= helper[hright]:
                Array[curr] = helper[hleft]
                hleft += 1
            else:
                Array[curr] = helper[hright]
                hright += 1
            curr += 1

        remaining = middle - hleft
        for i in range(remaining):
            Array[curr + i] = helper[hleft + i] 



if __name__ == "__main__":

    obj = SquareArray()
    result = obj.sortedSquares([-4,-1,0,3,10])
    print(result)