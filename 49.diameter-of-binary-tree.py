from typing import Optional
from ds_types.tree import Tree, TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal diameter
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1

        diameter = 0  
        dfs(root)
        return diameter
    
    

tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
Solution.diameterOfBinaryTree("", )

#       1        height 3
#    2           height 2
#   3 4          height 1
#  5   6         height 0

# Bottom up working to remove repetitive work
# By convention:


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # performs a depth-first search traversal of the binary tree and updates the `diameter` variable along the way
        # Post-order DFS
        def dfs(root):
            nonlocal diameter
            if root is None:
                return 0
            # Heights
            # ** Post-order DFS, searching left and right node before doing a operation
            left = dfs(root.left)
            right = dfs(root.right)

            # gist is we only care about max between diameter and height
            # avoiding repetitive work, we go from bottom up
            diameter = max(diameter, left + right)

            # returning the height/depth of the tree
            return max(left, right) + 1

        diameter = 0  
        dfs(root)
        return diameter