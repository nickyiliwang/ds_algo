# There are three main orders in which a tree can be traversed: pre-order, in-order, and post-order.

# Pre-order
# Visits the root node first, then the nodes in the left subtree, and finally the nodes in the right subtree. The order of visiting the nodes in the left and right subtrees is not specified.

# Usage: creating a copy of the tree

# In-order
# traversal visits the nodes in the left subtree, then the root node, and finally the nodes in the right subtree.

# Usage: sorting elements stored in the tree

# Post-order
# traversal visits the nodes in the left subtree, then the nodes in the right subtree, and finally the root node.
# Usage: deleting the tree

# Visualization
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

# Pre-order: 1 2 4 5 3 6 7
# In-order: 4 2 5 1 6 3 7
# Post-order: 4 5 2 6 7 3 1

# Breath first search
# Pre-order traversal

# Pre-order traversal starts by visiting the root node, then recursively visits the left subtree in pre-order, and finally recursively visits the right subtree in pre-order.

def preOrder(root):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

# Depth first search
# In-order traversal

# In-order traversal starts by recursively visiting the left subtree in in-order, then visits the root node, and finally recursively visits the right subtree in in-order.

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

# Depth first search
# Post-order traversal

# Post-order traversal starts by recursively visiting the left subtree in post-order, then recursively visits the right subtree in post-order, and finally visits the root node.
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)
        

# BFS is a graph traversal technique that systematically explores all the vertices of a graph level by level. It starts at the root (or source node) and explores its neighbors before moving on to the next level. It can be implemented using a queue data structure.

# DFS is another graph traversal technique that explores as far as possible along each branch before backtracking. It can be implemented using a stack (for iterative approach) or the system call stack (for recursive approach).

# Stack                 Queue

# DFS                   BFS
# 1. Pre-order          1. Level order
# 2. In-order
# 3. Post-order










# The relationship between the three binary tree traversals (pre-order, in-order, and post-order) and BFS and DFS is that pre-order and post-order traversals are essentially forms of DFS, while in-order traversal does not directly correspond to either BFS or DFS.

# Pre-order traversal is similar to DFS (using a stack) because it explores the nodes depth-first. It visits a node, then visits its left subtree, and finally visits its right subtree. This is equivalent to exploring the tree in a top-down, left-to-right manner.

# In-order traversal does not directly correspond to either BFS or DFS because it follows a different order. It visits the left subtree, then visits the root node, and finally visits the right subtree. In terms of searching algorithms, it is more related to binary search.

# Post-order traversal is also similar to DFS, but it explores the nodes from the bottom-up. It visits the left subtree, then visits the right subtree, and finally visits the root node. This is equivalent to exploring the tree in a bottom-up manner, visiting leaf nodes first.

# pre-order and post-order traversals can be viewed as forms of DFS 
# while in-order traversal has its own distinct order that does not align with BFS or DFS.