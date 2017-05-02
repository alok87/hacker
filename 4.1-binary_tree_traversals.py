class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


# Left, Node, Right
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)

# Node, Left, Right
def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)

# Left, Right, Node
def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)


    print("In order")
    print_inorder(root)

    print("\nPre order")
    print_preorder(root)

    print("\nPost order")
    print_postorder(root)
