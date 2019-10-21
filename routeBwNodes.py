class Graph:
    def __init__(self, vertices, edges):
        n = len(vertices)
        self.matrix = [[0 for x in range(n)] for y in range(n)]
        self.vertices = vertices
        self.edge = edges
        for edge in edges:
            x = vertices.index(edge[0])
            y = vertices.index(edge[1])
            self.matrix[x][y] = edge[2]

    def findPath(self):
                 




if __name__ == "__main__":

    graph = Graph([0,1,2,3,4,5],
                    [(0,1,1), 
                    (0,4,1),
                    (0,5,1),
                    (1,3,1),
                    (1,4,1),
                    (2,1,1),
                    (3,2,1),
                    (3,4,1)])