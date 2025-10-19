class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows - 1, -1, -1):
            if matrix[i][0] <= target:
                l = 0
                r = cols - 1

                while l <= r:
                    m = l + (r - l) // 2

                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] < target:
                        l = m + 1
                    else:
                        r = m - 1

        return False