from typing import Optional
from ds_types.tree import Tree, TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = invertTree(root.right),  invertTree(root.left)

    return root


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
invertTree(tree.root)
tree.printTree()
#     3
#  4      0
# 8     2
#      1
