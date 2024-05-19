#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
from typing import List, Optional
from collections import deque


# @lc code=start
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        q = deque([root])
        rightSide = []

        while q:
            tmp = []

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if len(tmp) > 0:
                rightSide.append(tmp[-1])

        return rightSide


# @lc code=end
