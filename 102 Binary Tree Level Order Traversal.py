class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# iteration
import collections
class Solution:
    def levelOrder(self, root: TreeNode):
        levels = []
        level = 0
        if not root:
            return None
        queue = collections.deque([root])

        while queue:
            levels.append([])
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return levels


# bfs
class Solution:
    def levelOrder(self, root: TreeNode):
        levels = []
        if not root:
            return levels

        def bfs(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)

        bfs(root, 0)
        return levels