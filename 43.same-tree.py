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

# recursive

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # true if both are same None
    if p is None and q is None:
        return True

    # False is one of them is not None
    if p is None or q is None:
        return False

    # False if the value are different
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     stack1 = [p]
#     stack2 = [q]

#     while stack1:
#         tree1 = stack1.pop()
#         tree2 = stack2.pop()
#         if tree1 is not None and tree2 is not None:
#             print("tree1", tree1.val)
#             print("tree2", tree2.val)
#             if tree1.val == tree2.val:
#                 stack1.append(tree1.left)
#                 stack1.append(tree1.right)

#                 stack2.append(tree2.left)
#                 stack2.append(tree2.right)

#             else:
#                 return False

#     return True


tree1 = Tree()
tree1.insert(3)
tree1.insert(4)
tree1.insert(0)
tree1.insert(8)
tree1.insert(2)
tree1.insert(1)
# different
tree1.insert(9)

# tree1.printTree()
#     3
#  0      4
#    2      8
#  1
tree2 = Tree()
tree2.insert(3)
tree2.insert(4)
tree2.insert(0)
tree2.insert(8)
tree2.insert(2)
tree2.insert(1)

print(isSameTree(tree1.root, tree2.root))
