class Solution:
    def process(self, idx):
        if not self.s:
            return None, 0
        value = ""
        while idx < self.size and self.s[idx] not in "()":
            value += self.s[idx]
            idx+=1
        node = TreeNode(val=int(value))
        if idx < self.size:
            if self.s[idx] == "(":
                node.left, idx = self.process(idx+1)
        if idx < self.size:
            if self.s[idx] == "(":
                node.right, idx = self.process(idx+1)
        return node, idx+1

    def str2tree(self, s: str) -> TreeNode:
        self.size = len(s)
        self.s = s
        root, idx = self.process(0)
        return root




# ----------------------------


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        ## RC ##
        ## APPROACH : RECURSION ##
        ## EDGE CASE : 1. NEGATIVE NODE VALUES ##
        ## 2. SINGLE NODE VALUES CAN BE MULTPLE DIGITS 12, 123..etc ##

        def dfs(s):
            if not s: return None  # empty string

            start = 0
            while (start < len(s) and s[start] != "("):  # until our first brace, whole string is node value
                start += 1

            node = TreeNode(s[0:start])
            if len(s) == start: return node  # no more characters, single node

            l, r = 0, 0
            for i in range(start, len(s)):
                if s[i] == "(": l += 1
                if s[i] == ")": r += 1
                if l == r: break

            node.left = dfs(s[start + 1:i])
            node.right = dfs(s[i + 2:-1])
            return node

        return dfs(s)