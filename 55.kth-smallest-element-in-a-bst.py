from typing import Optional
from ds_types.tree import Tree, TreeNode

# recursive, most straight forward, bit more Memory used
def kthSmallest(root: Optional[TreeNode], k: int) -> int:

    def traverse(node, res):
        if node:
            traverse(node.left, res)
            res.append(node.val)
            traverse(node.right, res)

    result = []
    traverse(root, result)

    print(result)
    return result[k - 1]


# # Iterative, no real advantage it seems
# def kthSmallest(root: Optional[TreeNode], k: int) -> int:
#     n = 0
#     stack = []
#     curr = root

#     while curr and stack:
#         while curr:
#             # keep going left will lead to the smallest value
#             stack.append(curr)
#             curr = curr.left

#         stack.pop()  # LIFO
#         # Finding the answer
#         n += 1
#         if n == k:
#             return curr.val

#         curr = curr.right

tree = Tree()
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(2)
# tree.printTree()
print(kthSmallest(tree.root, 1))
