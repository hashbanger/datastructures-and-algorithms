# finding the inorder successor of a binary search tree by storing parent node as well
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insertion(self, new_data):
        if self.data:

            # if the new node is smaller then go left
            if new_data < self.data:

                # if the left is empty then insert
                if self.left is None:
                    new_node = BinaryTree(new_data)
                    self.left = new_node
                    new_node.parent = self

                # otherwise recursively go to the left till empty spot is found
                else:
                    self.left.insertion(new_data)

            # if the node is greater then go right
            elif new_data > self.data:

                # if the right is empty then insert
                if self.right is None:
                    new_node = BinaryTree(new_data)
                    self.right = new_node
                    new_node.parent = self

                # otherwise recursively go to the right till empty spot is found
                else:
                    self.right.insertion(new_data)

            # raise error otherwise for duplicates
            else:
                print(f"Node {new_data} already exists.")
                return
        else:
            self.data = new_data


def _find_node(tree, key):

    # if the root is not None and not equal to the key then
    while (tree is not None) and (tree.data != key):

        # go to left if the key is smaller
        if key < tree.data:
            if tree.left is not None:
                tree = tree.left

        # otherwise go to right
        else:
            if tree.right is not None:
                tree = tree.right

    return tree


def _get_min_node(tree):
    current = tree

    # keep going to extreme left until it becomes None
    while current is not None:
        if current.left is None:
            break

        current = current.left

    return current


def _find_inorder_successor(tree):
    current = tree

    # if there is a right child then
    if current.right:

        # go to right and find the minimum value
        return _get_min_node(tree.right)

    # if there is no right child go to parent
    parent = current.parent

    # until parent exists
    while parent is not None:

        # if current is right child means parent is already visited
        # so we keep going back to parents until current not right child
        if current != parent.right:
            break

        current = parent
        parent = parent.parent

    return parent


def get_inorder_successor(tree, key):

    # first we find the node with the searched key
    key_node = _find_node(tree, key)

    # finding the inorder successor for the found node
    return _find_inorder_successor(key_node)


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

    key = 24
    inorder_successor = get_inorder_successor(bstree, key)
    print(f"Inorder Successor of {key} is {inorder_successor.data}")

    key = 44
    inorder_successor = get_inorder_successor(bstree, key)
    print(f"Inorder Successor of {key} is {inorder_successor.data}")

    key = 35
    inorder_successor = get_inorder_successor(bstree, key)
    print(f"Inorder Successor of {key} is {inorder_successor.data}")
