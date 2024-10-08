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

from ds_types.tree import TreeNode
from typing import Optional
from collections import deque


# @lc code=start
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  # need this
            return 0

        q = deque([root])
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()

                # just do this all the time
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res


# @lc code=end


# recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# iterative DFS (pre-ordered)
def maxDepth(root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    res = 0
    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res
