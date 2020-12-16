
def sumNumbers(root):
    root_to_leaf = 0
    stack = [(root, 0)]
    while stack:
        node, value = stack.pop()
        if node is not None:
            value = value*10 + node.val
                if node.left is None and node.right is None:
                    root_to_leaf += value
                else:
                    stack.append((root.left, value))
                    stack.append((root.right, value))
    return root_to_leaf


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