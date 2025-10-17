class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        mp = defaultdict(bool)
        res = ""
        for word in words:
            if len(word) == 1 or mp[word[:-1]]:
                mp[word] = True
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res