# @lc app=leetcode id=572 lang=python3

from typing import Optional
from ds_types.tree import TreeNode

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# @lc code=start
class Solution:
    def sameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        else:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # empty subRoot will always be part of a tree
        if not subRoot:
            return True

        #  but if root is None, subRoot cannot be the subtree
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end
