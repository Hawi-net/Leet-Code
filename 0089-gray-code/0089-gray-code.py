class Solution:
    def grayCode(self, n: int) -> List[int]:
        output = []
        integers = 2**n
        
        for i in range(integers):
            output.append(i ^ (i >> 1))
            
        return output