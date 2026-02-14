class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_sorted = sorted([x for x, _ in points])
        return max(x2 - x1 for x1, x2 in itertools.pairwise(x_sorted))        