class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node: return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        vals = []
        dfs(root)
        counts = Counter(vals)
        mx = max(counts.values())
        return [x for x, v in counts.items() if v == mx]