# checking if a binary tree is a subtree of another binary tree
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


def _check_identical(tree, subtree):

    # if both are none then subtree is part of the tree
    if (tree is None) and (subtree is None):
        return True

    # if only one of them is None then result is false
    if (tree is None) or (subtree is None):
        return False

    # recursively check all the children
    return (
        (tree.data == subtree.data)
        and (_check_identical(tree.left, subtree.left))
        and (_check_identical(tree.right, subtree.right))
    )


def check_subtree(tree, subtree):

    # if the subtree is empty then it is part of the tree
    if subtree is None:
        return True

    if tree is None:
        return False

    # checking if the root is identical and the rest of the tree
    if _check_identical(tree, subtree):
        return True

    # if current node doesn't match with the root of subtree try for left and right child of the tree recursively
    return check_subtree(tree.left, subtree) or check_subtree(tree.right, subtree)


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

    sbtree1 = BinaryTree(10)
    sbtree1.insertion(4)
    sbtree1.insertion(12)
    sbtree1.insertion(2)

    sbtree2 = BinaryTree(10)
    sbtree2.insertion(4)
    sbtree2.insertion(13)
    sbtree2.insertion(2)

    print("\nChecking subtree 1:", check_subtree(btree, sbtree1))
    print("Checking subtree 2:", check_subtree(btree, sbtree2))
