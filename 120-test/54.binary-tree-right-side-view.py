# [199] Binary Tree Right Side View

from typing import List, Optional
from collections import deque
from ds_types.tree import TreeNode

# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.


# Key:
# BST level order traversal with queue
# while adding the res from the loop, only add the right most value, which is tmp[-1]


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
