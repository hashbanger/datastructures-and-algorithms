# calculating the maximum width of a binary tree using preorder traversal.
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertion(self, new_data):
        if self.data:

            # if the new node is smaller then go left
            if new_data < self.data:

                # if the left is empty then insert
                if self.left is None:
                    self.left = BinaryTree(new_data)

                # otherwise recursively go to the left till empty spot is found
                else:
                    self.left.insertion(new_data)

            # if the node is greater then go right
            elif new_data > self.data:

                # if the right is empty then insert
                if self.right is None:
                    self.right = BinaryTree(new_data)

                # otherwise recursively go to the right till empty spot is found
                else:
                    self.right.insertion(new_data)

            # raise error otherwise for duplicates
            else:
                print(f"Node {new_data} already exists.")
                return
        else:
            self.data = new_data


def _get_height(tree):
    if tree is None:
        return 0

    # recursively visit the left child if it exists
    left_height = _get_height(tree.left)

    # recursively visit the right child if it exists
    right_height = _get_height(tree.right)

    # the larger one would be considered the height at the current node
    return 1 + max(left_height, right_height)


def _get_level_width(tree, counts, level):
    if tree is not None:

        # increase the node counts for the curernt level
        counts[level] += 1
        _get_level_width(tree.left, counts, level + 1)
        _get_level_width(tree.right, counts, level + 1)


def get_max_width(tree):
    height = _get_height(tree)

    counts = [0] * height

    # start with the first level
    level = 0

    _get_level_width(tree, counts, level)

    return max(counts)


if __name__ == "__main__":
    btree = BinaryTree(25)
    btree.insertion(15)
    btree.insertion(50)
    btree.insertion(10)
    btree.insertion(22)
    btree.insertion(35)
    btree.insertion(70)
    btree.insertion(4)
    btree.insertion(12)
    btree.insertion(18)
    btree.insertion(24)
    btree.insertion(31)
    btree.insertion(44)
    btree.insertion(66)
    btree.insertion(90)
    btree.insertion(2)

    print("\nMax Level Width:", get_max_width(btree))

    btree = BinaryTree(10)
    btree.insertion(8)
    btree.insertion(11)
    btree.insertion(5)
    btree.insertion(9)
    btree.insertion(12)
    btree.insertion(6)

    print("\nMax Level Width:", get_max_width(btree))
