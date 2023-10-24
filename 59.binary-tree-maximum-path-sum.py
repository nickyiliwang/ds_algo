from typing import Optional, List
from ds_types.tree import Tree, TreeNode

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return
            print(root.val)
            dfs(root.left)
            dfs(root.right)
                
        dfs(root)

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution.maxPathSum("", root))
