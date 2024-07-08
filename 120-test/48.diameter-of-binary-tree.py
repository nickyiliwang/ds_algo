# @lc app=leetcode id=543 lang=python3

from typing import Optional
from ds_types.tree import TreeNode

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# @lc code=start
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

# @lc code=end
