from typing import Optional
from ds_types.tree import Tree, TreeNode

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# # recursive, most straight forward, bit more Memory used
# def kthSmallest(root: Optional[TreeNode], k: int) -> int:

#     def traverse(node, res):
#         if node:
#             traverse(node.left, res)
#             res.append(node.val)
#             traverse(node.right, res)

#     result = []
#     traverse(root, result)

#     print(result)
#     return result[k - 1]


# Iterative
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    n = 0
    stack = []
    curr = root

    while curr and stack:
        while curr:
            # keep going left will lead to the smallest value
            stack.append(curr)
            curr = curr.left

        stack.pop()  # LIFO
        # Finding the answer
        n += 1
        if n == k:
            return curr.val

        curr = curr.right


tree = Tree()
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(2)
# tree.printTree()
print(kthSmallest(tree.root, 1))
