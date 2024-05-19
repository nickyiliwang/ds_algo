from typing import Optional
from ds_types.tree import TreeNode


# in-order traversal and appending value in a bst
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
