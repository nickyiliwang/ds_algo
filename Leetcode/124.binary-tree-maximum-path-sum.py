#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (39.81%)
# Likes:    16072
# Dislikes: 701
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty
# path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
#
#
#

from typing import Optional, List
from tree import Tree, TreeNode


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        maxPath = [root.val]

        def dfs(root):
            if not root:
                return

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # since left and right nodes can be negative numbers and they are optional so we need 0 to make them optional
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # max path sum WITH split but we are not passing this to the root
            maxPath = max(maxPath, root.val + leftMax + rightMax)

            # max path without split
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return maxPath


# @lc code=end

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution.maxPathSum("", root))
