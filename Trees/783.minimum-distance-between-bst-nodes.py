#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (59.55%)
# Likes:    3465
# Dislikes: 417
# Total Accepted:    251.5K
# Total Submissions: 422.4K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum difference
# between the values of any two different nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 10^5
#
#
#
# Note: This question is the same as 530:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)
        return res


# @lc code=end


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        values = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        idx = 0
        while idx + 1 < len(values):
            res = min(res, values[idx + 1] - values[idx])
            idx += 1

        return res
