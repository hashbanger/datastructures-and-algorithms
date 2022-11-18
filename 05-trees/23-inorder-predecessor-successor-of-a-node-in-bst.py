# finding the inorder predecessor of a node in a binary search tree
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
    if tree:

        # recursively iterate in the left direction
        inorder_traversal(tree.left)

        # output the root value
        print(tree.data, end=" ")

        # recursively iterate in the right direction
        inorder_traversal(tree.right)


# def static_variables(identifier, value):
#     def decorate(func):
#         setattr(func, identifier, value)
#         return func

#     return decorate


# @static_variables("predecessor", None)
# @static_variables("successor", None)
def get_predecessor_and_successor(tree, key):
    if tree is None:
        return

    # if the key if found then
    if tree.data == key:

        # and if it has left child then
        if tree.left is not None:

            # we make one left then we go to extreme right
            temp = tree.left
            while temp.right:
                temp = temp.right

            get_predecessor_and_successor.predecessor = temp.data

        # and if it has right child then
        if tree.right is not None:

            # we make one right then we go to extreme left
            temp = tree.right
            while temp.left:
                temp = temp.left

            get_predecessor_and_successor.successor = temp.data

        return

    # if the key is smaller
    if key < tree.data:

        # we assign current as the sucessor and recursively apply on left child
        get_predecessor_and_successor.successor = tree.data
        get_predecessor_and_successor(tree.left, key)

    # if the key is greater
    else:

        # we assign current as the predecessor and recursively apply on right child
        get_predecessor_and_successor.predecessor = tree.data
        get_predecessor_and_successor(tree.right, key)


if __name__ == "__main__":
    bstree = BinaryTree(25)
    bstree.insertion(15)
    bstree.insertion(50)
    bstree.insertion(10)
    bstree.insertion(22)
    bstree.insertion(35)
    bstree.insertion(70)
    bstree.insertion(4)
    bstree.insertion(12)
    bstree.insertion(18)
    bstree.insertion(24)
    bstree.insertion(31)
    bstree.insertion(44)
    bstree.insertion(66)
    bstree.insertion(90)
    bstree.insertion(2)

    print("Inorder Traversal:")
    inorder_traversal(bstree)

    # checking for key that doesn't exist in the tree, expected is an approximate position
    key = 67
    get_predecessor_and_successor.predecessor = None
    get_predecessor_and_successor.successor = None
    get_predecessor_and_successor(bstree, key)

    print(f"\n\nInorder Predessor of {key}:", get_predecessor_and_successor.predecessor)
    print(f"Inorder Successor of {key}:", get_predecessor_and_successor.successor)

    # checking for a normal key which has children nodes
    key = 31
    get_predecessor_and_successor.predecessor = None
    get_predecessor_and_successor.successor = None
    get_predecessor_and_successor(bstree, key)

    print(f"\nInorder Predessor of {key}:", get_predecessor_and_successor.predecessor)
    print(f"Inorder Successor of {key}:", get_predecessor_and_successor.successor)

    # checking for a leaf node
    key = 2
    get_predecessor_and_successor.predecessor = None
    get_predecessor_and_successor.successor = None
    get_predecessor_and_successor(bstree, key)

    print(f"\nInorder Predessor of {key}:", get_predecessor_and_successor.predecessor)
    print(f"Inorder Successor of {key}:", get_predecessor_and_successor.successor)
