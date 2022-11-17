# checking if a binary tree is a subtree of another binary tree
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next_right = None

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


def _connect_recursive(tree):
    if tree is None:
        return

    if tree.left:
        tree.left.next_right = tree.right

    if tree.right:
        if tree.next_right:
            tree.right.next_right = tree.next_right.left
        else:
            tree.right.next_right = None

    _connect_recursive(tree.left)
    _connect_recursive(tree.right)


def connect_level_nodes(tree):
    tree.next_right = None

    _connect_recursive(tree)


def inorder_traversal(tree):
    if tree is None:
        return

    # recursively visit the left child until its None
    inorder_traversal(tree.left)

    # if the tree has a level node on its right then print it
    if tree.next_right:
        print(f"{tree.data}->(r={tree.next_right.data})", end=" ")
    else:
        print(tree.data, end=" ")

    # recursively visit the right child until its None
    inorder_traversal(tree.right)


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

    print("\n\nConnecting level Nodes")
    connect_level_nodes(btree)
    inorder_traversal(btree)

    print("\n")
    btree = BinaryTree(10)
    btree.insertion(8)
    btree.insertion(11)
    btree.insertion(5)
    btree.insertion(9)
    btree.insertion(12)
    btree.insertion(6)

    print("\nInorder Traversal:")
    inorder_traversal(btree)

    print("\n\nConnecting level Nodes")
    connect_level_nodes(btree)
    inorder_traversal(btree)
