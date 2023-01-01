from typing import Optional
from ds_types.tree import Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# iterative DFS passes 167 / 182 testcases
# falls short when encountering:
# root: [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2], subRoot: [1,null,1,null,1,null,1,null,1,null,1,2] <- returns False when it's True

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if root.val != subRoot.val:
        return False

    res = False

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.val == subRoot.val:
                res = sameTree(node, subRoot)
            stack.append(node.left)
            stack.append(node.right)

    return res

def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
    if p is None and q is None:
        return True

    if p is None or q is None or p.val != q.val:
        return False

    return sameTree(p.left, q.left) and sameTree(p.right, q.right)


tree1 = Tree()
tree1.insert(1)
tree1.insert(1)

# tree1.printTree()
#     3
#  0      4
#    2      8
#  1
tree2 = Tree()
tree2.insert(1)

print(isSubtree(tree1.root, tree2.root))
