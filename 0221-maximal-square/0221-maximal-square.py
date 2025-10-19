class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS,COLS=len(matrix),len(matrix[0])

        dp=[[0 for _ in range(COLS)] for _ in range(ROWS)]
        max_area=0
        for i in range(ROWS):
            for j in range(COLS):
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])

                else:
                    if matrix[i][j]=="1":
                        dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                
                max_area=max(max_area,dp[i][j])
        
        return max_area**2