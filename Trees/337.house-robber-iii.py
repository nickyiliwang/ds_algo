#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (54.29%)
# Likes:    8485
# Dislikes: 140
# Total Accepted:    384.6K
# Total Submissions: 708.5K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree. It
# will automatically contact the police if two directly-linked houses were
# broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money the
# thief can rob without alerting the police.
#
#
# Example 1:
#
#
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4
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

# with root and without root in an modified dfs

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return [0, 0]

            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            withRoot = node.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]

        return max(dfs(root))


# @lc code=end
