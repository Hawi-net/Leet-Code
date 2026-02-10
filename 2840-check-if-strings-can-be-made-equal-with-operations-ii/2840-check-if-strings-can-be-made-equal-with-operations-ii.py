class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd, even, a = [0] * 26, [0] * 26, ord("a")
        for i in range(len(s1)):
            m = odd if i % 2 else even
            m[ord(s1[i]) - a] += 1
            m[ord(s2[i]) - a] -= 1
        return all(all(not v for v in m) for m in (even, odd))