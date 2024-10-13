#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (59.46%)
# Likes:    5783
# Dislikes: 466
# Total Accepted:    263.2K
# Total Submissions: 442.7K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
#
# Two trees are duplicate if they have the same structure with the same node
# values.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#
#
# Example 2:
#
#
# Input: root = [2,1,1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#
#
#
# Constraints:
#
#
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
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
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        # store the counter of each serialized subtree
        counter = defaultdict(list)
        res = []

        def dfs(node):
            if not node:
                return "#"

            st = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            # Any subsequent occurrences (third, fourth, etc.) will have a length greater than 1, but we are only interested in adding the subtree to the result list when we first identify it as a duplicate (i.e., the second occurrence).
            if len(counter[st]) == 1:
                res.append(node)

            counter[st].append(node)

            return st

        dfs(root)
        return res


# @lc code=end
