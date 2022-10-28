# traversing the tree in a breadth first method, all nodes of the same level first.
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


def inorder_traversal(tree):
    if tree is None:
        return

    # recursively visit the left child until its None
    inorder_traversal(tree.left)

    # output the root value
    print(tree.data, end=" ")

    # recursively visit the right child until its None
    inorder_traversal(tree.right)


def traverse_current_level(tree, level):
    if tree is None:
        return

    # level decreases recursively until final desired level is reached
    if level == 1:
        print(tree.data, end=" ")

    # if not reached to the level go one level below each side
    elif level > 1:

        # if left exisits recursively iterate to next level
        traverse_current_level(tree.left, level - 1)

        # if right exisits recursively iterate to next level
        traverse_current_level(tree.right, level - 1)


def get_height(tree):
    if tree is None:
        return -1

    # recursively visit the left child if it exists
    left_height = get_height(tree.left)

    # recursively visit the right child if it exists
    right_height = get_height(tree.right)

    # the larger one would be considered the height at the current node
    return 1 + max(left_height, right_height)


def breadth_first_traversal(tree):

    # get the height for the tree
    height = get_height(tree)

    # for each level traverse all the level nodes
    for h in range(0, height + 1):
        traverse_current_level(tree, h + 1)
        print()


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

    print("\nInorder Traversal:")
    inorder_traversal(btree)

    print("\n\nBreadth First Traversal:")
    breadth_first_traversal(btree)
