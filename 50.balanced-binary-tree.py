from typing import Optional
from ds_types.tree import Tree, TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        
        def dfs(root):
            nonlocal isBalanced
            
            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)

            if abs(left - right) > 1:
                isBalanced = False
            
            return max(left, right) + 1
        
        return isBalanced
 
# Explanation
# Just like diameter of a tree, this is a post-order traversal DFS
# we are checking left and right for height balance, from depth 
# we have a global var that stores the isBalanced check for each height
        

tree = Tree()
tree.insert(3)
tree.insert(9)
tree.insert(20)
tree.insert(15)
tree.insert(7)

print(
Solution.isBalanced("", tree)
)