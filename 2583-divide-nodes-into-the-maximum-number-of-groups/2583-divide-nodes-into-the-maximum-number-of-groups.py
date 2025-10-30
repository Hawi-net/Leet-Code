from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        def eccentricity(s):
            d = [-1] * (n + 1)
            d[s] = 0
            q = deque([s])
            best = 0
            while q:
                u = q.popleft()
                best = max(best, d[u])
                for v in graph[u]:
                    if d[v] == -1:
                        d[v] = d[u] + 1
                        q.append(v)
            return best
        
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        col = [0] * (n + 1)
        seen = [False] * (n + 1)
        comps = []
        for i in range(1, n + 1):
            if not seen[i]:
                q = deque([i])
                seen[i] = True
                col[i] = 1
                comp = [i]
                ok = True
                while q and ok:
                    u = q.popleft()
                    for v in graph[u]:
                        if not seen[v]:
                            seen[v] = True
                            col[v] = -col[u]
                            q.append(v)
                            comp.append(v)
                        elif col[v] == col[u]:
                            ok = False
                            break
                if not ok:
                    return -1
                comps.append(comp)
        
        ans = 0
        for comp in comps:
            curr = 0
            for u in comp:
                curr = max(curr, eccentricity(u) + 1)
            ans += curr
        return ans