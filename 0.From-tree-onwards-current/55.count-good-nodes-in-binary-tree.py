from typing import *
from collections import deque
from ds_types.tree import Tree, TreeNode

# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
#
# Given a binary tree root, a node X in the tree is named good if in the path
# from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
# 
# Time:
# Space:

# @lc code=start
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

# @lc code=end
tree = Tree()
tree.insert(3)
tree.insert(3)
tree.insert(4)
tree.insert(2)
print(Solution.goodNodes("", tree.root))
