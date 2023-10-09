from ds_types.tree import Tree, TreeNode


def postorder_traversal(root):
    # create an empty stack and push the root node
    stack = []
    stack.append(root)

    # create an empty list to store the post-order traversal
    post_order = []

    # while the stack is not empty
    while stack:
        # pop the top node from the stack
        node = stack.pop()

        # add the node's value to the post-order list
        post_order.append(node.val)

        # push the node's children, if any, onto the stack
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    print(post_order)

    # reverse the post-order list to get the final post-order traversal
    post_order = post_order[::-1]
    return post_order


tree = Tree()
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(2)
print(postorder_traversal(tree.root))
