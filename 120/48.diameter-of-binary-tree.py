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
from ds_types.tree import TreeNode


# @lc code=start
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0

        def dfs(node):
            nonlocal dia
            if node is None:
                return 0

            left, right = dfs(node.left), dfs(node.right)

            # update diameter with max height of left + right
            dia = max(dia, left + right)

            # returning the height/depth of the tree
            return 1 + max(left, right)

        dfs(root)
        return dia


# @lc code=end

# https://www.youtube.com/watch?v=K81C31ytOZE
