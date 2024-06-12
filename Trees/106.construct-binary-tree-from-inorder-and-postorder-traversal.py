#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (63.16%)
# Likes:    7950
# Dislikes: 130
# Total Accepted:    647.6K
# Total Submissions: 1M
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
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


# using inorder index dict for lookup O(1)
# the last node of post order is the root
#
# left index crossing the right index is the base case, return Null
# instead of passing in subsets, we use l/r pointers
# building the right node then left node
#
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {v: i for i, v in enumerate(inorder)}

        def builder(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())

            i = inorderIndex[root.val]
            root.right = builder(i + 1, r)
            root.left = builder(l, i - 1)

            return root

        return builder(0, len(inorder) - 1)


# @lc code=end


# based on this idea, O(n ^ 2)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        i = inorder.index(root.val)

        root.right = self.buildTree(inorder[i + 1 :], postorder)
        root.left = self.buildTree(inorder[:i], postorder)

        return root
