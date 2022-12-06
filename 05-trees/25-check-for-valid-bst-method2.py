# INCOMPLETE
# check if the binary tree is a valid BST or not using inorder traversal
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(tree):
    previous_node = None
    return _check_valid_bst(tree, previous_node)


# def _check_valid_bst(tree, previous_node):
#     if tree is not None:
#         if _check_valid_bst(tree.left, previous_node) == True:
#             return False

#         if (previous_node is not None) and (tree.data <= previous_node.data):
#             return False

#         previous_node = tree

#         return _check_valid_bst(tree.right, previous_node)

#     return True


if __name__ == "__main__":
    bstree = BinaryTree(25)
    bstree.left = BinaryTree(15)
    bstree.left.left = BinaryTree(10)
    bstree.left.right = BinaryTree(20)
    bstree.right = BinaryTree(30)
    bstree.right.left = BinaryTree(27)

    print("Checking Validity:", is_valid_bst(bstree))

    btree = BinaryTree(25)
    btree.left = BinaryTree(15)
    btree.left.left = BinaryTree(30)
    btree.left.right = BinaryTree(20)
    btree.right = BinaryTree(30)
    btree.right.left = BinaryTree(27)

    print("Checking Validity:", is_valid_bst(btree))
