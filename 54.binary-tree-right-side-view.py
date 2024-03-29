from typing import *
from collections import deque
from ds_types.tree import Tree, TreeNode


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return res
    q = deque([root])
    res = [root.val]

    while q:
        tmp = []
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                tmp.append(node.left.val)
                q.append(node.left)
            if node.right:
                tmp.append(node.right.val)
                q.append(node.right)

        if len(tmp) > 0:
            res.append(
                tmp[-1]
            )  # only difference from order level traversal is we only want the right most node, so tmp[-1] gets us that
    return res


tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
print(rightSideView(tree.root))

# I'm so fucking good
