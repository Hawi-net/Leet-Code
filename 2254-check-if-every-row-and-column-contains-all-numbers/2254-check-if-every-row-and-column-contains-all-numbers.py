class Solution:
    def checkValid(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            row = matrix[i]
            if (set(range(1, n+1)).difference(set(row)) != set()):
                return False

        for j in range(0, n):
            col = [matrix[i][j] for i in range(0, m)]
            if (set(range(1, n+1)).difference(set(col)) != set()):
                return False
        
        return True