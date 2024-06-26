def inorderTraversal(root):
    stack = []
    result = []
    current = root

    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)
            current = current.left

        # Current must be None at this point
        current = stack.pop()
        result.append(current.val)

        # Visit the right subtree
        current = current.right

    return result


def preorderTraversal(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right and then left to the stack so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def postorderTraversal(root):
    if root is None:
        return []

    stack = []
    result = []
    last_visited = None
    current = root

    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)
            current = current.left

        # Peek the node from the stack
        current = stack[-1]

        # If the right subtree is not yet processed
        if current.right is None or current.right == last_visited:
            current = stack.pop()
            result.append(current.val)
            last_visited = current
            current = None
        else:
            # Process the right subtree
            current = current.right

    return result
