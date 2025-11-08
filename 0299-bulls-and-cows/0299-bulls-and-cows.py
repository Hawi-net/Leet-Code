class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = c = 0
        ds = Counter(secret)
        dg = Counter(guess)

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                b += 1
                ds[guess[i]] -= 1
                dg[guess[i]] -= 1
        
        for k in dg:
            if dg[k] > 0 and k in ds and ds[k] > 0:
                c += min(dg[k], ds[k])
        
        return str(b) + 'A' + str(c) + 'B'