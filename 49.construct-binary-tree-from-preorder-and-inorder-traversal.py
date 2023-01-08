from typing import Optional, List

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# problem description and tactics
# For preorder:
# 1. First value is always the root
# 2. The sub-array minus the root value needs the inorder list to determine the left and right values
# 3. We know that inorder mean that it goes from left to right


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:

    def array_to_tree(left, right):
        nonlocal preorder_index
        # this condition says if left index is bigger than right
        # there's nothing to be done
        # because if we see for "9" on index 0
        # left and right root of the tree will not pass this condition

        # For root.left
        # inorder_index_map[9] - 1 becomes (0 - 1)
        # left remains 0, right is -1 returning None

        # For root.right
        # inorder_index_map[9] + 1 becomes (0 + 1)
        # left is 1, right is 0, left is still bigger than right, the algo will not continue
        if left > right: return None

        # select the preorder_index element as the root and increment it
        root_value = preorder[preorder_index]
        root = TreeNode(root_value)

        preorder_index += 1

        # build left and right subtree
        # excluding inorder_index_map[root_value] element because it's the root
        root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
        root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

        return root

    preorder_index = 0

    # build a hashmap to store value -> its index relations
    # {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
    inorder_index_map = {inorder[i]: i for i in range(len(inorder))}

    return array_to_tree(0, len(preorder) - 1)


root = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])


def printTree(node):
    if not node:
        return None

    if node:
        print(node.val)
        printTree(node.left)
        printTree(node.right)


printTree(root)

# def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#     if not preorder or not inorder:
#         return None

#     # {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
#     inorder_hash = {inorder[i]: i for i in range(len(inorder))}

#     def _buildTree(preorder, inorder_start, inorder_end):
#         if inorder_start > inorder_end:
#             return None

#         root = TreeNode(preorder[0])

#         mid = inorder_hash[preorder[0]]

#         # recursively build left subtree
#         # preorder[1:mid + 1]: start idx 1 ignoring the root, end at (mid + 1), not including (mid + 1)
#         # inorder_start
#         root.left = _buildTree(preorder[1:mid + 1], inorder_start, mid - 1)
#         root.right = _buildTree(preorder[mid + 1:], mid + 1, inorder_end)
#         return root

#     return _buildTree(preorder, 0, len(inorder) - 1)

# # below code constructs an example of a tree
# def buildTree(preorder: List[int], inorder: List[int],
#               root) -> Optional[TreeNode]:
#     if not root:
#         return

#     buildTree(preorder, inorder, root.left)
#     print(root.val)
#     buildTree(preorder, inorder, root.right)

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], root)
