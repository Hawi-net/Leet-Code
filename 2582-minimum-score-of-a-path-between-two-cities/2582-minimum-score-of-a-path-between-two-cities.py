class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for src,dst,dis in roads:
            adj[src].append((dst,dis))
            adj[dst].append((src,dis))
        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal answer
            for nei,dis in adj[i]:
                answer=min(answer,dis)
                dfs(nei)
        visit,answer=set(),float('inf')
        dfs(n)
        return answer