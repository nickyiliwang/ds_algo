from typing import Optional
from collections import deque
from ds_types.tree import Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input: root = [2,1,3]
# Output: true
# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Using deque and lower and upper bounds

def isValidBST(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    q = deque([(root, -float('inf'), float('inf'))])
    while q:
        node, lower, upper = q.popleft()
        # Not a BST
        if not lower < node.val < upper:
            return False

        if node.left:
            # set parent node value as upper bound
            # meaning left node has to be smaller than upper bound
            q.append((node.left, lower, node.val))

        if node.right:
            # opposite as above, using paren node val as lower bound
            q.append((node.right, node.val, upper))

    return True


# Recursive approach

def isValidBST(root: Optional[TreeNode]) -> bool:

    def valid(node, lower, upper):
        if root is None:
            return True

        if not (lower < node.val < upper):
            return False

        return valid(node.left, lower, node.val) and valid(
            node.right, node.val, upper)

    return valid(root, -float("inf"), float("inf"))


# # Naive approach
# # Failed at root = [5,4,6,null,null,3,7]
# # It failed because we are not checking if the left and right child nodes are also valid BSTs
# # A BST is a tree where each node's value is greater than all the values in its left subtree, and less than all the values in its right subtree.
# def isValidBST(root: Optional[TreeNode]) -> bool:
#     q = deque([root])
#     while q:
#         for _ in range(len(q)):
#             node = q.popleft()
#             parent = node.val
#             if node.left:
#                 if node.val > node.left.val:
#                     q.append(node.left)
#                 else:
#                     return False
#             if node.right:
#                 if node.val < node.right.val:
#                     q.append(node.right)
#                 else:
#                     return False

#     return True

tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
# tree.printTree()

print(isValidBST(tree.root))

# Long form explanation of the deque solution
# This implementation uses a deque to store a tuple for each node, consisting of the node, a lower bound on the node's value, and an upper bound on the node's value. The lower and upper bounds are used to ensure that the node's value is within the valid range for a BST.

# The deque is initialized with a tuple for the root node, with the lower and upper bounds set to negative infinity and positive infinity, respectively. This allows the root node to have any value, as long as it is within the bounds of the left and right subtrees.

# The implementation then enters a loop that processes the nodes in the deque. For each node, it checks if the node's value is within the valid range specified by the lower and upper bounds. If the value is not within the range, it returns False immediately. If the value is within the range, it adds the left and right child nodes (if they exist) to the deque, with the appropriate lower and upper bounds set based on the value of the parent node.

# Finally, after the deque is empty, the function returns True to indicate that the tree is a valid BST.

# ChatGPT wrote this, I do not understand, pretty confusing to remember too. Here for reference
# class Solution:

#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True

#         if root.left and not self.isValidBST(root.left):
#             return False

#         if root.right and not self.isValidBST(root.right):
#             return False

#         if root.left and root.val <= root.left.val:
#             return False

#         if root.right and root.val >= root.right.val:
#             return False

#         return True

# # This implementation first checks if the root node is None, in which case it returns True since an empty tree is considered a valid BST.
# # It then checks the left and right child nodes to see if they are valid BSTs, and returns False if either of them is not.
# # Finally, it checks the parent node's value against the values of the left and right child nodes, and returns False if the parent's value is not greater than the left child's value and less than the right child's value.
