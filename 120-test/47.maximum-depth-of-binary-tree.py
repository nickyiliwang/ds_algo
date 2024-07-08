#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# Maybe try a iterative approach

from ds_types.tree import TreeNode
from typing import Optional

# @lc code=start
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

# @lc code=end