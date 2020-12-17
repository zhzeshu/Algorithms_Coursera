import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):

        values = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            l = len(queue)
            i = 0
            n = 0
            for _ in range(l):
                node = queue.popleft()
                i += 1
                n += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(n / i)

        return values