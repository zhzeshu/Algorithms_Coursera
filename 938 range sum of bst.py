class TreeNode:
    def __init__(self,val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(root, left, right):
        self.ans = 0
        def dfs(node):
            if not node:
                return None
            if left <= node.val <= right:
                self.ans += node.val
            if left < node.val:
                dfs(node.left)
            if node.val < right:
                dfs(node.right)

        dfs(root)
        return self.ans


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)

        return ans