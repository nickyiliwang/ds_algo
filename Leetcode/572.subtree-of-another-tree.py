#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
#
#
#



# @lc code=start
class Solution:
    def sameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        else:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end
