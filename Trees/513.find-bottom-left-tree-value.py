#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (71.19%)
# Likes:    3773
# Dislikes: 294
# Total Accepted:    360.5K
# Total Submissions: 506.4K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = root.val

        q = deque([root])

        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if tmp:
                res = tmp[0]

        return res


# @lc code=end
