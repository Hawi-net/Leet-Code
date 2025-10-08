class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        l=maxx=0
        my_set=set()
        my_set.add(word[0])
        for r in range(1,len(word)):
            if word[r]<word[r-1]:
                my_set=set()
                l=r
            if word[r] not in my_set:
                my_set.add(word[r])
            if len(my_set)==5:
                maxx=max(maxx,r-l+1)
        return maxx       
                
            
        
        