#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Medium (69.14%)
# Likes:    5223
# Dislikes: 175
# Total Accepted:    303.1K
# Total Submissions: 436.5K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# the sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#
# Example 2:
#
#
# Input: root = [0,null,1]
# Output: [1,null,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
#
#
#
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# key:
# reversed inorder traversal
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = 0

        def dfs(node):
            nonlocal curr
            if not node:
                return

            dfs(node.right)
            tmp = node.val
            node.val += curr
            curr += tmp
            dfs(node.left)

            return node

        return dfs(root)


# @lc code=end
