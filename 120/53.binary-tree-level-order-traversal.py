# @lc app=leetcode id=102 lang=python3

from typing import Optional, List
from collections import deque
from ds_types.tree import TreeNode

# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).


# Key:
# Classic BFS with queues
# remember to use a loop in the while loop for left and right nodes


# @lc code=start
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if len(tmp) > 0:
                res.append(tmp)
        return res


# @lc code=end
