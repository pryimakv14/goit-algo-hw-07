class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    
    def __str__(self):
        return str(self.val)


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current


def sum_value_node(node):
    if node.left is None and node.right is None:
        return node.val

    left = sum_value_node(node.left) if node.left else 0
    right = sum_value_node(node.right) if node.right else 0

    return left + node.val + right


root = Node(5)
root = insert(root, 1)
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 16)
root = insert(root, 8)
root = insert(root, 100)
root = insert(root, 6)
root = insert(root, 9)

print("Task 1: max value: ", max_value_node(root))
print("Task 2: min value: ", min_value_node(root))
print("Task 3: sum: ", sum_value_node(root))
