# @lc app=leetcode id=98 lang=python3
from typing import Optional
from collections import deque
from ds_types.tree import Tree, TreeNode
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# Input: root = [2,1,3]
# Output: true

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# try it with iteratively

# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

# @lc code=end
