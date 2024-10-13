#
# @lc app=leetcode id=1325 lang=python3
#
# [1325] Delete Leaves With a Given Value
#
# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/
#
# algorithms
# Medium (77.51%)
# Likes:    2718
# Dislikes: 54
# Total Accepted:    209.8K
# Total Submissions: 270.7K
# Testcase Example:  '[1,2,3,2,null,2,4]\n2'
#
# Given a binary tree root and an integer target, delete all the leaf nodes
# with value target.
#
# Note that once you delete a leaf node with value target, if its parent node
# becomes a leaf node and has the value target, it should also be deleted (you
# need to continue doing that until you cannot).
#
#
# Example 1:
#
#
#
#
# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture
# in left).
# After removing, new nodes become leaf nodes with value (target = 2) (Picture
# in center).
#
#
# Example 2:
#
#
#
#
# Input: root = [1,3,3,3,2], target = 3
# Output: [1,3,null,null,2]
#
#
# Example 3:
#
#
#
#
# Input: root = [1,2,null,2,null,2], target = 2
# Output: [1]
# Explanation: Leaf nodes in green with value (target = 2) are removed at each
# step.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3000].
# 1 <= Node.val, target <= 1000
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


# postorder for delete
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.left and not node.right and node.val == target:
                return None
            else:
                return node

        return dfs(root)


# @lc code=end
