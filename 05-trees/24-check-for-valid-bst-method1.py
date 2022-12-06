# check if the binary tree is a valid BST or not
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(tree):

    # defining limits
    INT_MAX = 99999
    INT_MIN = -99999
    return _check_valid_bst(tree, INT_MIN, INT_MAX)


def _check_valid_bst(tree, min_value, max_value):

    # if there is no node tree is valid
    if tree is None:
        return True

    # if the node is out of valid range based on parent value return False
    if tree.data < min_value or tree.data > max_value:
        return False

    # iteratively check on the left and right for valid ranges
    return _check_valid_bst(tree.left, min_value, tree.data - 1) and _check_valid_bst(
        tree.right, tree.data + 1, max_value
    )


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
    btree.right.left = BinaryTree(9)

    print("Checking Validity:", is_valid_bst(btree))
