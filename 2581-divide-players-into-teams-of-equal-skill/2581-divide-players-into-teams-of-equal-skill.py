class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        chemistry = 0
        target = skill[0] + skill[-1]

        for i in range(n // 2):
            if skill[i] + skill[-i-1] != target:
                return -1
            chemistry += skill[i] * skill[-i-1] 
        return chemistry

       

       