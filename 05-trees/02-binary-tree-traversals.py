class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root_node):
    if root_node:

        # recursively iterate in the left direction
        inorder_traversal(root_node.left)

        # output the root value
        print(root_node.data, end=" ")

        # recursively iterate in the right direction
        inorder_traversal(root_node.right)


def preorder_traversal(root_node):
    if root_node:

        # output the root value
        print(root_node.data, end=" ")

        # recursively iterate in the left direction
        preorder_traversal(root_node.left)

        # recursively iterate in the right direction
        preorder_traversal(root_node.right)


def postorder_traversal(root_node):
    if root_node:

        # recursively iterate in the left direction
        postorder_traversal(root_node.left)

        # recursively iterate in the right direction
        postorder_traversal(root_node.right)

        # output the root value
        print(root_node.data, end=" ")


if __name__ == "__main__":
    btree = Node(1)
    btree.left = Node(2)
    btree.right = Node(3)
    btree.left.left = Node(4)
    btree.left.right = Node(5)

    print("\nInorder: ")
    inorder_traversal(btree)
    print("\nPreorder: ")
    preorder_traversal(btree)
    print("\nPostorder: ")
    postorder_traversal(btree)
