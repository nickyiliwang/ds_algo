# @lc app=leetcode id=98 lang=python3
from typing import Optional
from collections import deque
from ds_types.tree import Tree, TreeNode


# Recursive approach, DFS

# Key:
# return valid(node.left, low, node.val) and valid(node.right, node.val, high)
# when going down the tree, we need to update the high or upper limit of the value
# bc left val cannot exceed the upper bound, which is the parent node val


# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

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
                node, low, high = q.popleft()

                if not low < node.val < high:
                    return False

                if node.left:
                    # left node, update high bound since it cannot be bigger than parent node
                    q.append((node.left, low, node.val))

                if node.right:
                    # right node, update the low bound since it cannot be smaller than parent node
                    q.append((node.right, node.val, high))

        return True
