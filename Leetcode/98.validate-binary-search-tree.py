#
# @lc app=leetcode id=98 lang=python3
# @lc code=start
# @lc code=start
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
# A valid BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
from typing import Optional


# @lc code=start
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


# @lc code=end
