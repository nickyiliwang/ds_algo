# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        print(self.root)
        return self.root

    def insert(self, val):
        if self.root is not None:
            self._insert(val, self.root)
        else:
            self.root = TreeNode(val)

    def _insert(self, val, node):
        if val < node.val:
            if node.left:
                self._insert(val, node.left)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(val, node.right)
            else:
                node.right = TreeNode(val)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node.val)
            self._printTree(node.right)


# tree = Tree()
# tree.insert(3)
# tree.insert(4)
# tree.insert(0)
# tree.insert(8)
# tree.insert(2)
# tree.printTree()
