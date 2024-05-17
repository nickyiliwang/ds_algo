# @lc app=leetcode id=110 lang=python3

from typing import Optional
from ds_types.tree import Tree, TreeNode

# Key
# Like diameter of a tree, post-order traversal DFS
# check left and right for height balance with the abs difference
# difference greater than 1 is considered unbalanced because we are allowing 1 height for child nodes


# @lc code=start
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

            return max(left, right) + 1

        dfs(root)

        return isBalanced


# @lc code=end
