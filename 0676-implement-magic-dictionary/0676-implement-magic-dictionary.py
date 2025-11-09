class MagicDictionary:

    def __init__(self):
        self.map = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                key = word[0:i] + '_' + word[i+1:]
                
                if not key in self.map:
                    self.map[key] = []
                
                self.map[key].append(word[i])
        
    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            key = searchWord[0:i] + '_' + searchWord[i+1:]
            
            if key not in self.map: 
                continue
            
            for c in self.map[key]:
                if c != searchWord[i]:
                    return True
        
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)