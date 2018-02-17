def max(a, b):
    if a > b:
        return a
    else:
        return b


def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1
