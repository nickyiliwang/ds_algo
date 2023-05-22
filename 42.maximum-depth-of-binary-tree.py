from typing import Optional
from ds_types.tree import Tree, TreeNode
from collections import deque

# recursive DFS
# T: O(n), M: O(n)


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# iterative DFS (pre-ordered)
def maxDepth(root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    res = 0
    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res

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
