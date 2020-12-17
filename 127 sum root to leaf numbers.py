# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root, 0)]
        while stack:
            node, value = stack.pop()
            if node is not None:
                value = value * 10 + node.val
                if node.left is None and node.right is None:
                    root_to_leaf += value
                else:
                    stack.append((root.right, value))
                    stack.append((root.left, value))

        return root_to_leaf




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, value):
            if node:
                value = value * 10 + node.val
                if not node.left and not node.right:
                    self.ans += value
                else:
                    dfs(node.left, value)
                    dfs(node.right, value)

        dfs(root, 0)

        return self.ans