
from typing import Optional
from typing import List
from collections import deque
from ds_types.tree import Tree, TreeNode

# DFS does not have the right order
# T: O(n), M: O(n/2) -> O(n)

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    q = deque([root])
    res = [[root.val]]

    while q:
        tmp = []  # captures all nodes in a level

        for _ in range(len(q)):
            node = q.popleft()
            if (node.left):
                q.append(node.left)
                tmp.append(node.left.val)
            if (node.right):
                q.append(node.right)
                tmp.append(node.right.val)

        if len(tmp) > 0:
            res.append(tmp)

    return res

# Explanation
# Queue because FIFO, and to check each levels
# Start with the root node
# for each node in the range(len(q)), ie. maybe a level has 4 or more nodes in a level, check them all 
# while the queue is none empty we check the left and right node
# for each node, put back the left and right child node for next iteration
# we do not want empty levels to be added into the result


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
