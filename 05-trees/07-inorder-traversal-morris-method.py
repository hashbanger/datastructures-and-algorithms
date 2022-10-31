# Traversing a binary tree without recursion or stack, using morris traversal which is space efficient.
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


def morris_traversal(tree):
    current = tree

    # until the current is not None
    while current:

        # if the left child does not exist then visit and move to its right
        if current.left is None:
            print(current.data, end=" ")
            current = current.right

        else:

            # otherwise find the predecessor to connect the threads to parent node
            pred = current.left
            while (pred.right is not None) and (pred.right != current):
                pred = pred.right

            # if there is no thread then add one and move current to left child
            if pred.right is None:
                pred.right = current
                current = current.left

            # if the thread already exists then remove it and visit the current and move to right
            else:
                pred.right = None
                print(current.data, end=" ")
                current = current.right


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

    print("\nInorder Traversal with recursion:")
    inorder_traversal(btree)

    print("\n\nInorder Traversal using Morris:")
    morris_traversal(btree)
    print()

    btree = BinaryTree(10)
    btree.insertion(8)
    btree.insertion(9)
    btree.insertion(11)
    btree.insertion(12)
    btree.insertion(5)
    btree.insertion(6)

    print("\nInorder Traversal with recursion:")
    inorder_traversal(btree)

    print("\n\nInorder Traversal using Morris:")
    morris_traversal(btree)
