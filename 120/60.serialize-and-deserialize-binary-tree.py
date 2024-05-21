# @lc app=leetcode id=297 lang=python3
from ds_types.tree import TreeNode

# Key:
# Can use preorder for both serialize and deserialize
# use a index to traverse the data and deserialize


# @lc code=start
class Codec:
    def serialize(self, root):
        serialize = []

        def dfs(root):
            nonlocal serialize
            if not root:
                serialize.append("None")
                return
            serialize.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root

        dfs(root)
        return ",".join(serialize)

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
