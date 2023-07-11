
from typing import Optional
from typing import List
from collections import deque
from ds_types.tree import Tree


# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS does not have the right order

# T: O(n), M: O(n/2) -> O(n)


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = [[root.val]]

    while q:
        # why is it outside the for loop?
        # for every new iteration of the while loop, tmp is empty
        tmp = []  # captures all nodes in a level

        # why use range(len(q)) ?
        # we have left and right child nodes in each parent
        for _ in range(len(q)):
            node = q.popleft()
            if (node.left):
                q.append(node.left)
                tmp.append(node.left.val)
            if (node.right):
                q.append(node.right)
                tmp.append(node.right.val)
        # why is res.append out side for loop ?
        # want the loop of left and right nodes to finish
        if len(tmp) > 0:
            res.append(tmp)

    return res

# # other solution
# def levelOrder( root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         q = deque()
#         q.append(root)

#         while q:
#             tmp = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node:
#                     tmp.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if len(tmp) > 0:
#                 res.append(tmp)

#         return res

# # DFS does not have the right order
# def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
#     stack = [root]
#     res = [[root.val]]

#     while stack:
#         node = stack.pop()
#         if node:
#             stack.append(node.left)
#             stack.append(node.right)
#             tmp = []

#             if node.left:
#                 tmp.append(node.left.val)
#             if node.right:
#                 tmp.append(node.right.val)

#             res.append(tmp)

#     return res
#     # OUTPUT: [[6], [2, 8], [7, 9], [], [], [0, 4], [3, 5], [], [], []]


# tree = Tree()
# tree.insert(6)
# tree.insert(2)
# tree.insert(8)
# tree.insert(0)
# tree.insert(4)
# tree.insert(7)
# tree.insert(9)
# tree.insert(3)
# tree.insert(5)
# tree.printTree()
#           6
#        2      8
#      0   4  7   9
#        3   5

tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
print(
    levelOrder(tree.root)
)
