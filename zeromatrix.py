class ZeroMatrix:
    def __init__(self, length):
        self.length = length
        self.storematrix = [[] for i in range(length)]
        

    def storeZeros(self, matrix):
        for i in range(self.length):
            for j in range(self.length):
                if matrix[i][j] == 0:
                    self.storematrix[i][j]= True


