# @lc app=leetcode id=230 lang=python3
from typing import Optional
from ds_types.tree import TreeNode


# in-order traversal and appending value in a bst
# @lc code=start
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if len(res) == k:
                return
            res.append(node.val)
            dfs(node.right)

        dfs(root)

        return res[-1]


# @lc code=end


# with stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
