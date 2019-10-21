class matrixRotation:
    def __init__(self, length):
        self.length = length
        pass

    def rotate(self,matrix):
        if len(matrix) == 0 or len(matrix) != len(matrix[0]):
            return False
        
        for layer in range(int(len(matrix)/2)):
            
            first = layer
            last = self.length -1 - layer

            i = first

            for i in range(last):
                offset = i - first
                top = matrix[first][i]

                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = top

        return matrix


if __name__ == "__main__":
    obj = matrixRotation(3)
    matrix = [[1,2,3],[5,6,7],[9,10,11]]
    print(obj.rotate(matrix))


