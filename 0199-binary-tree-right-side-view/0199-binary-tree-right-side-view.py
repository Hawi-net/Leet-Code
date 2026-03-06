class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(node.val) # last in this level
        return res