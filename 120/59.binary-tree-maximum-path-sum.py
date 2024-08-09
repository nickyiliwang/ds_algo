# @lc app=leetcode id=124 lang=python3
from typing import Optional, List
from ds_types.tree import TreeNode

# Given the root of a binary tree, return the maximum path sum of any non-empty path

# Key
# Post order traversal


# @lc code=start
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val

        def dfs(node):
            nonlocal maxPath

            if not node:
                return 0

            leftMax, rightMax = dfs(node.left), dfs(node.right)

            # To clear negative numbers
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            maxPath = max(maxPath, node.val + leftMax + rightMax)

            # bottom up, so able to add upon previous levels
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return maxPath


# @lc code=end
