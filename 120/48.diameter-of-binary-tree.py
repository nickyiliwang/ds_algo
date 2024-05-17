# @lc app=leetcode id=543 lang=python3

from typing import Optional


#       1        height 3
#    2           height 2
#   3 4          height 1
#  5   6         height 0

# Key:
# Bottom up working to remove repetitive work
# performs a depth-first search traversal of the binary tree and updates the `diameter` variable along the way
# avoiding repetitive work, we go from bottom up
# Post-order DFS


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal diameter
            if root is None:
                return 0

            # Heights
            left = dfs(root.left)
            right = dfs(root.right)

            # only care about the max between the previous height
            diameter = max(diameter, left + right)

            # returning the height/depth of the tree
            return 1 + max(left, right)

        diameter = 0
        dfs(root)
        return diameter


# @lc code=end
