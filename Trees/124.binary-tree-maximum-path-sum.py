#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (40.15%)
# Likes:    16531
# Dislikes: 732
# Total Accepted:    1.3M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
# 
# The path sum of a path is the sum of the node's values in the path.
# 
# Given the root of a binary tree, return the maximum path sum of any non-empty
# path.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
# 
# 
# Example 2:
# 
# 
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
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
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val

        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            
            left =dfs(node.left)
            right= dfs(node.right)

            left = max(left, 0)
            right = max(right, 0)

            maxPath = max(maxPath, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)

        return maxPath

            


            

        
# @lc code=end

