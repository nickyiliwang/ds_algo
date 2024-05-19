# @lc app=leetcode id=98 lang=python3
from typing import Optional
from collections import deque
from ds_types.tree import Tree, TreeNode


# Recursive approach, DFS
# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lower, upper):
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            return valid(node.left, lower, node.val) and valid(
                node.right, node.val, upper
            )

        return valid(root, float("-inf"), float("inf"))


# @lc code=end


# Using deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            for _ in range(len(q)):
                node, lower, upper = q.popleft()

                if not lower < node.val < upper:
                    return False

                if node.left:
                    # left node, update upper bound since it cannot be bigger than parent node
                    q.append((node.left, lower, node.val))

                if node.right:
                    # right node, update the lower bound since it cannot be smaller than parent node
                    q.append((node.right, node.val, upper))

        return True
