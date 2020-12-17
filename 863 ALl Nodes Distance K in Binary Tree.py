# Definition for a binary tree node.

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}

        while queue:
            if queue[0][1] == K:
                return [node.val for node, q in queue]
            node, d = queue.popleft()

            for nod in (node.left, node.right, node.par):
                if nod and nod not in seen:
                    seen.add(nod)
                    queue.append((nod, d + 1))
        return []
