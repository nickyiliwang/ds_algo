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
def preOrder(root):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

# Depth first search
# In-order traversal
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

# Depth first search
# Post-order traversal
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)