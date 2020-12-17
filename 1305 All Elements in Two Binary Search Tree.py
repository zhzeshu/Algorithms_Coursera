import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        all_elements = []

        queue = collections.deque()

        if root1:
            queue.append(root1)
        if root2:
            queue.append(root2)

        while queue:
            node = queue.popleft()
            all_elements.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return sorted(all_elements)


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.arr1, self.arr2 = [], []
        self.inorder(root1, self.arr1)
        self.inorder(root2, self.arr2)

        return self.merge2list(self.arr1, self.arr2)

    def inorder(self, root, arr):
        if root == None:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def merge2list(self, arr1, arr2):
        res = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        if i < len(arr1):
            res += arr1[i:]
        if j < len(arr2):
            res += arr2[j:]
        return res