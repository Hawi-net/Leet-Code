class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        ans = [0 for _ in range(len(A))]
        B_Q = deque(sorted([(b, i) for i, b in enumerate(B)]))
        for a in sorted(A):
            _, i = B_Q.popleft() if a > B_Q[0][0] else B_Q.pop()
            ans[i] = a
        return ans