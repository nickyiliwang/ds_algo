# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (66.95%)
# Likes:    2283
# Dislikes: 96
# Total Accepted:    147.6K
# Total Submissions: 220.4K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
#
# Given the roots of two binary trees root1 and root2, return true if the two
# trees are flip equivalent or false otherwise.
#
#
# Example 1:
#
#
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
#
#
# Example 2:
#
#
# Input: root1 = [], root2 = []
# Output: true
#
#
# Example 3:
#
#
# Input: root1 = [], root2 = [1]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree is in the range [0, 100].
# Each tree will have unique node values in the range [0, 99].
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

# 72/77 cases passed (N/A)
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q1 = deque([root1])
        q2 = deque([root2])

        while q1 or q2:
            tmp1 = []
            tmp2 = []
            if len(q1) != len(q2):
                return False

            for _ in range(len(q1)):
                node1 = q1.popleft()
                node2 = q2.popleft()

                if node1:
                    tmp1.append(node1.val)
                    q1.append(node1.left)
                    q1.append(node1.right)
                else:
                    tmp1.append(0)

                if node2:
                    tmp2.append(node2.val)
                    q2.append(node2.left)
                    q2.append(node2.right)
                else:
                    tmp2.append(0)

            if tmp1 or tmp2:
                if sum(tmp1) != sum(tmp2):
                    return False
                elif len(tmp1) != len(tmp2):
                    return False

        return True


# @lc code=end
