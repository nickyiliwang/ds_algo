#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (72.61%)
# Likes:    11317
# Dislikes: 225
# Total Accepted:    1.4M
# Total Submissions: 2M
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given the root of a binary search tree, and an integer k, return the k^th
# smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete
# operations) and you need to find the kth smallest frequently, how would you
# optimize?
#
#


# @lc code=start
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node, res):
            if node:
                inOrder(node.left, res)
                res.append(node.val)
                inOrder(node.right, res)

            return res

        res = inOrder(root, [])
        return res[k - 1]


# @lc code=end
