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
        inorderDict = {v: i for i, v in enumerate(inorder)}

        def builder(l, r):
            if l > r:
                return None

            root = TreeNode(preorder.pop(0))
            i = inorderDict[root.val]

            root.left = builder(l, i - 1)
            root.right = builder(i + 1, r)

            return root

        return builder(0, len(inorder) - 1)


# @lc code=end
