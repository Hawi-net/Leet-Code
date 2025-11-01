class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0,int(c**0.5) + 1):
            b_sq = c - a*a
            if b_sq < 0:
                break
            b = int(b_sq**0.5)
            if b*b ==b_sq:
                return True
        return False
        
        