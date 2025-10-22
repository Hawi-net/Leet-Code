class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        for i in range(12):
            for j in range(60):
                if((bin(i)+bin(j)).count('1')==turnedOn):
                    k='%d:%02d' %(i, j)
                    print(k)
                    res.append(k)

        return res