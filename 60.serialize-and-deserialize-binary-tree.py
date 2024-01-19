class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
        print(serialize)
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


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

tree = Codec.deserialize("", Codec.serialize("", root))
