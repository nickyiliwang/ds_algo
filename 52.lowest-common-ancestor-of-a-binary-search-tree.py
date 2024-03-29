from typing import Optional
from ds_types.tree import Tree

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).


# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2


# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# T: O(logN), because we only visit one node for every level of the tree, so the height of the tree
# S: O(1), not using any to store values


def lowestCommonAncestor(
    root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
) -> Optional[TreeNode]:
    curr = root

    # for LCA that has a node same as the LCA
    # node1 = TreeNode(6) <- same as LCA
    # node2 = TreeNode(7)
    # 7 can go down the tree but their LCA is still 6 because of node1

    # going down the tree only choosing one path at a time

    while curr:
        if curr.val > p.val and curr.val > q.val:
            curr = curr.left
        elif curr.val < p.val and curr.val < q.val:
            curr = curr.right
        else:
            return curr


tree = Tree()
tree.insert(6)
tree.insert(2)
tree.insert(8)
tree.insert(0)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(3)
tree.insert(5)
# tree.printTree()
#           6
#        2      8
#      0   4  7   9
#        3   5
node1 = TreeNode(7)
node2 = TreeNode(9)
print(lowestCommonAncestor(tree.root, node1, node2))
