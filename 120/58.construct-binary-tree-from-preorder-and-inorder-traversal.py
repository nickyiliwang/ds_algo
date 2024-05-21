from ds_types.tree import TreeNode
from typing import List, Optional

# @lc app=leetcode id=105 lang=python3

# Key:
# First node in a preorder traversal is the root
# find the index of the root then we can recursively find the left and right leaf
# left will be in the left of the index
# right will be in the right of the index


# @lc code=start
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # pop left from preorder to get the root node val
            i = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[i])

            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i + 1 :])

            return root


# @lc code=end
