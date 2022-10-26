class Node:
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

    btree = Node(1)

    btree.left = Node(2)
    btree.right = Node(3)

    btree.left.left = Node(4)
