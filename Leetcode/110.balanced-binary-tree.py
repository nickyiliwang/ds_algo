#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (52.13%)
# Likes:    10545
# Dislikes: 672
# Total Accepted:    1.5M
# Total Submissions: 2.8M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(root):
            nonlocal isBalanced

            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)

            if abs(left - right) > 1:
                isBalanced = False

            return 1 + max(left, right)

        dfs(root)

        return isBalanced


# @lc code=end
