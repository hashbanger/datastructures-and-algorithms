class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


if __name__ == "__main__":
    # creating a sample tree below
    #          1
    #        /  \
    #       2    3
    #      /
    #     4

    btree = BinaryTree(1)

    btree.left = BinaryTree(2)
    btree.right = BinaryTree(3)

    btree.left.left = BinaryTree(4)
