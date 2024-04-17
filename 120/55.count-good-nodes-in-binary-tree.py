from typing import *
from collections import deque
from ds_types.tree import Tree, TreeNode


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
