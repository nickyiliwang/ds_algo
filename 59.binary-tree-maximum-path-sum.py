from typing import Optional, List
from ds_types.tree import Tree, TreeNode


def maxPathSum(root):
    maxPath = root.val

    def dfs(root):
        nonlocal maxPath
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        # since left and right nodes can be negative numbers and they are optional so we need 0 to make them optional
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # max path sum WITH split but we are not passing this to the root
        maxPath = max(maxPath, root.val + leftMax + rightMax)

        # max path without split
        return root.val + max(leftMax, rightMax)

    dfs(root)
    return maxPath


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.left = TreeNode(9)
root.left.left = TreeNode(24)
root.left.right = TreeNode(5)


print(maxPathSum(root))
