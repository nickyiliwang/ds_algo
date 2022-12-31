from typing import Optional
from ds_types.tree import Tree
from collections import deque

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive DFS
# T: O(n), M: O(n)
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# # iterative DFS (pre-ordered)
# def maxDepth(root: Optional[TreeNode]) -> int:
#     stack = [[root, 1]]
#     res = 0
#     while stack:
#         node, depth = stack.pop()

#         if node:
#             res = max(res, depth)
#             stack.append([node.left, depth + 1])
#             stack.append([node.right, depth + 1])

#     return res

# # iterative BFS (queue)
# # queue is FIFO
# def maxDepth(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0

#     level = 0

#     q = deque([root])
#     while q:
#         for i in range(len(q)):

#             node = q.popleft()  # removes from left
#             # check this node's left and right leaf nodes and add back to the queue
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)

#         level += 1
#     return level

tree = Tree()
tree.insert(3)
tree.insert(4)
tree.insert(0)
tree.insert(8)
tree.insert(2)
tree.insert(1)
# tree.printTree()
#     3
#  0      4
#    2      8
#  1
print(maxDepth(tree.root))
