# finding the lowest common ancestor in a bst through iterative approac
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


def get_lowest_common_ancestor(tree, first_node, second_node):
    while tree is not None:

        # if both of the nodes are smaller then go left otherwise
        if (first_node.data < tree.data) and (second_node.data < tree.data):
            tree = tree.left

        # go right if both are greater
        elif (first_node.data > tree.data) and (second_node.data > tree.data):
            tree = tree.right

        else:
            break

    return tree


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

    first_node = BinaryTree(18)
    second_node = BinaryTree(24)
    print(
        f"Lowest Common Ancestor of {first_node.data} and {second_node.data} is",
        get_lowest_common_ancestor(bstree, first_node, second_node).data,
    )

    first_node = BinaryTree(15)
    second_node = BinaryTree(24)
    print(
        f"Lowest Common Ancestor of {first_node.data} and {second_node.data} is",
        get_lowest_common_ancestor(bstree, first_node, second_node).data,
    )

    first_node = BinaryTree(50)
    second_node = BinaryTree(90)
    print(
        f"Lowest Common Ancestor of {first_node.data} and {second_node.data} is",
        get_lowest_common_ancestor(bstree, first_node, second_node).data,
    )
