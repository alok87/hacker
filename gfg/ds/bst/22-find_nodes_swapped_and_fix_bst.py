class Node:
    """Class to represent a single node
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_node_in_bst(root, node):
    """Insert a 'node' in existing tree having root 'root'
    """
    if not root:
        root = node
        return

    if node.val > root.val:
        if not root.right:
            root.right = node
            return
        else:
            insert_node_in_bst(root.right, node)
    elif node.val < root.val:
        if not root.left:
            root.left = node
            return
        else:
            insert_node_in_bst(root.left, node)
    else:
        print("[Warning] Node %s is already inserted, can not have duplicate nodes in Binary Search Tree" % node.val)
        return


def print_inorder(root):
    """Prints the binary tree in inorder traversal ==> Left, Node, Right
    """
    if not root:
        return
    print_inorder(root.left)
    print(root.val)
    print_inorder(root.right)


def get_elements(root):
    """Returns a list of elements in a binary tree in sorted order (ASC)
    """
    if not root:
        return []
    return get_elements(root.left) + [root.val] + get_elements(root.right)


def swap_two_elements(root):
    """Swaps two elements in a binary search tree
    """
    if not root:
        return
    swap_two_elements(root.left)
    if root.val == 7:
        root.val = 8
    elif root.val == 8:
        root.val = 7
    else:
        pass
    swap_two_elements(root.right)


def find_swapped_elements(swapped_array):
    first = None
    first_index = None
    last = None
    i = 0
    while i < len(swapped_array) - 2:
        if swapped_array[i + 1] < swapped_array[i]:
            if not first:
                first = swapped_array[i]
                first_index = i
                i += 1
                continue
            if not last:
                last = swapped_array[i]
        i += 1
    if not last:
        last = swapped_array[first_index + 1]
    return first, last


def fix_bst(root, c, d):
    if not root:
        return
    fix_bst(root.left, c, d)
    if root.val == c:
        root.val = d
    elif root.val == d:
        root.val = c
    else:
        pass
    fix_bst(root.right, d, c)


if __name__ == '__main__':
    root = Node(10)
    binary_tree = None

    for val in [3, 5, 7, 8, 15, 20, 25]:
        insert_node_in_bst(root, Node(val))

    elements = get_elements(root)
    print("BST: %s" % elements)

    swap_two_elements(root)

    swapped_elements = get_elements(root)
    print("Swapped BST: %s" % swapped_elements)

    c, d = find_swapped_elements(swapped_elements)
    print("Swapped elements are %d %d" % (c, d))

    fix_bst(root, c, d)
    print("Fixed BST: %s" % get_elements(root))


