# @lc app=leetcode id=100 lang=python3

from typing import Optional
from ds_types.tree import TreeNode


# recursive DFS
# @lc code=start
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @lc code=end


# DFS with stack
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]

        while stack:
            p, q = stack.pop()

            if p and q and p.val == q.val:
                stack.append([p.left, q.left])
                stack.append([p.right, q.right])

            elif p or q:
                return False

        return True
