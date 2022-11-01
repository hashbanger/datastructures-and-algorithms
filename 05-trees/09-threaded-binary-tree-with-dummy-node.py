# implementing a threaded binary tree where the left of the node points to inorder predecessor and
# right of the node points to inorder successor
# we add a dummy node at the top that can be pointed to when the thread has to point to None
class ThreadedBinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # these will be switched to False if the node has respective child,
        # and not thread to predecessor/successor
        self.left_thread = True
        self.right_thread = True


def insertion(tree, new_data):

    current = tree
    parent = None

    # we iterate till we find the parent to add the child to
    while current.data is not None:
        if current.data == new_data:
            print("Duplicate Key")
            return tree

        parent = current

        # if the data is less than current then check
        if new_data < current.data:

            # if the current has a left child then move on to the child
            if current.left_thread == False:
                current = current.left

            # otherwise we stop and move to adding new node as child
            else:
                break

        # if the data is more than current then check
        else:

            # if the current has a right child, then move on to the child
            if current.right_thread == False:
                current = current.right

            # otherwise we stop and move to adding the new node as child
            else:
                break

    new_node = ThreadedBinaryTree(new_data)

    # if there is only dummy node, (or are no nodes present) we add a new node pointing to None
    if current.data is None:

        tree = new_node
        tree.left = current
        tree.right = current

        # this is the dummy node that has None as data
        # we make this so that these can be pointed to by the left most and right most nodes of the tree
        # since in principle the left most node would have left thread true so
        # it can't have None as child so it must have thread pointing to None node.
        current.left = tree
        current.right = current
        current.left_thread = False
        current.right_thread = False

        return tree

    # if the node is a left child
    elif new_data < current.data:

        # node's left points to inorder predecessor (for leftmost it's None)
        # node's right points to inorder successor
        new_node.left = parent.left
        new_node.right = parent

        # parent's left is not a thread anymore but a child
        # add the child's link on the left
        parent.left_thread = False
        parent.left = new_node

    # if the node is a right child
    else:

        # node's right points to inorder successor (for rightmost it's None)
        # node's left points to inorder predecessor
        new_node.left = parent
        new_node.right = parent.right

        # parent's right is not a thread anymore but a child
        # add the child's link on the right
        parent.right_thread = False
        parent.right = new_node


def _find_inorder_successor(ptr):

    # if the node has right thread then we just return the successor
    if ptr.right_thread == True:
        return ptr.right

    # otherwise we move to the right subtree then to it's leftmost node
    tree = ptr.right
    while tree.left_thread == False:
        tree = tree.left

    return tree


def inorder_traverse_threaded_binary_tree(tree):
    if tree.data is None:
        print("Empty Tree.")
        return None

    # first we reach the leftmost node of the tree
    ptr = tree
    while ptr.left_thread == False:
        ptr = ptr.left

    # we keep finding the inorder successor and print
    while ptr.data is not None:
        print(ptr.data, end=" ")
        ptr = _find_inorder_successor(ptr)


def preorder_traverse_threaded_binary_tree(tree):
    ptr = tree
    while ptr.data is not None:
        print(ptr.data, end=" ")

        # if there is a left child then we move to left
        if ptr.left_thread == False:
            ptr = ptr.left
        else:
            # otherwise keep moving back using the right threads until right child exists for a node
            while (ptr.data is not None) and (ptr.right_thread == True):
                ptr = ptr.right

            # if there is a right child then move to right
            if (ptr.data is not None) and (ptr.right_thread == False):
                ptr = ptr.right


if __name__ == "__main__":
    tbtree = ThreadedBinaryTree(None)  # creating dummy node with None data

    tbtree = insertion(tbtree, 10)
    insertion(tbtree, 8)
    insertion(tbtree, 11)
    insertion(tbtree, 12)
    insertion(tbtree, 9)
    insertion(tbtree, 5)
    insertion(tbtree, 6)

    print("\n\nThreaded Binary Tree Inorder Traversal: ")
    inorder_traverse_threaded_binary_tree(tbtree)

    print("\n\nThreaded Binary Tree Preorder Traversal: ")
    preorder_traverse_threaded_binary_tree(tbtree)

    tbtree = ThreadedBinaryTree(None)
    tbtree = insertion(tbtree, 25)
    insertion(tbtree, 15)
    insertion(tbtree, 50)
    insertion(tbtree, 10)
    insertion(tbtree, 22)
    insertion(tbtree, 35)
    insertion(tbtree, 70)
    insertion(tbtree, 4)
    insertion(tbtree, 12)
    insertion(tbtree, 18)
    insertion(tbtree, 24)
    insertion(tbtree, 31)
    insertion(tbtree, 44)
    insertion(tbtree, 66)
    insertion(tbtree, 90)
    insertion(tbtree, 2)

    print("\n\nThreaded Binary Tree Inorder Traversal: ")
    inorder_traverse_threaded_binary_tree(tbtree)

    print("\n\nThreaded Binary Tree Preorder Traversal: ")
    preorder_traverse_threaded_binary_tree(tbtree)
