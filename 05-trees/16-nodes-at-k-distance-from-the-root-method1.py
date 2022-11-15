# printing all the nodes that are at k distance from the root
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


def k_distance_nodes(tree, level):
    if tree is None:
        return

    if level == 1:
        print(tree.data, end=" ")
    elif level > 1:
        k_distance_nodes(tree.left, level - 1)
        k_distance_nodes(tree.right, level - 1)


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

    k = 2
    print(f"\nNodes at {k} distance from root:")
    k_distance_nodes(btree, k + 1)

    btree = BinaryTree(10)
    btree.insertion(8)
    btree.insertion(11)
    btree.insertion(5)
    btree.insertion(9)
    btree.insertion(12)
    btree.insertion(6)

    k = 3
    print(f"\nNodes at {k} distance from root:")
    k_distance_nodes(btree, k + 1)
