class MergeSort:
    def __init__(self):
        pass

    def mergeSort(self, Array, low, high):
        if low < high:
            mid = (low + high)//2
            self.mergeSort(Array, low, mid)
            self.mergeSort(Array, mid + 1, high)
            self.merge(Array, mid, low, high)

    def merge(Array, middle, low, high):
        pass