#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (56.32%)
# Likes:    9817
# Dislikes: 366
# Total Accepted:    822.9K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
#
#


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Codec:
    def serialize(self, root):
        serialized = []

        def dfs(root):
            nonlocal serialized
            if not root:
                serialized.append("None")
                return

            serialized.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(serialized)

    def deserialize(self, data):
        serial = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if serial[index] == "None":
                index += 1
                return None
            root = TreeNode(int(serial[index]))
            index += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()


# @lc code=end


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

tree = Codec.deserialize("", Codec.serialize("", root))


def dfs(root):
    if not root:
        return

    dfs(root.left)
    dfs(root.right)
    print(root.val)


dfs(tree)


# 13/53 cases passed (N/A)
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized = ""

        def dfs(root):
            nonlocal serialized
            if not root:
                return ""

            serialized += str(root.val) + ","
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        serial = data.split(",")
        root = None

        def insert(root, value):
            if root is None:
                return TreeNode(value)

            if value < root.val:
                root.left = insert(root.left, value)
            else:
                root.right = insert(root.right, value)
            return root

        for n in serial:
            if n != "":
                root = insert(root, int(n))

        return root
