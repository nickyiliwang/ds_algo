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

# Key:
# Need a maxVal value that keeps the max for next iteration
# current node must be bigger than or equal to be considered good
# remember the first value in the queue is an tuple (node, maxVal


# @lc code=start
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([(root, float("-inf"))])
        count = 0

        while q:
            for _ in range(len(q)):
                node, maxVal = q.popleft()

                if node:
                    if node.val >= maxVal:
                        count += 1

                    q.append((node.left, max(maxVal, node.val)))
                    q.append((node.right, max(maxVal, node.val)))
        return count


# @lc code=end


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0

            res = 1 if root.val <= maxVal else 0
            maxVal = max(root.val, maxVal)

            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)

            return res

        return dfs(root, root.val)


tree = Tree()
tree.insert(3)
tree.insert(3)
tree.insert(4)
tree.insert(2)
print(Solution.goodNodes("", tree.root))
