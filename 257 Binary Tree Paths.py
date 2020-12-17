
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePath(root):
    paths = []

    def dfs(node, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += '->'
                dfs(node.left, path)
                dfs(node.right, path)


    dfs(root, '')
    return paths



class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths