class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(root):
        if not root:
            return 0

        def recurse(node, node_min, node_max):
            if not node:
                return node_max - node_min
            node_min = min(node_min, node.val)
            node_max = max(node_max, node.val)

            left = recurse(node.left, node_min, node_max)
            right = recurse(node.right, node_min, node_max)

            return max(right, left)

        return recurse(root, root.val, root.val)