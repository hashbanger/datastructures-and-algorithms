# finding the diameter of the tree covering both possible cases, through the root node of not.
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


class Diameter:
    def __init__(self):
        self.diameter = 0

    def calculate_diameter(self, tree):
        if tree is None:
            return 0

        # iteratively visit the left and right child and get their diameter (heigh)
        left_diameter = self.calculate_diameter(tree.left)
        right_diameter = self.calculate_diameter(tree.right)

        # we calculate the diameter that passes through current node
        diameter_current_node = 1 + left_diameter + right_diameter

        # for other case where diameter could be larger we pass the max height including current node
        height_above_node = 1 + max(left_diameter, right_diameter)

        # updating the diameter to max of the existing one and calculated for current node
        self.diameter = max(self.diameter, diameter_current_node)

        return height_above_node

    def get_diameter(self, tree):
        self.calculate_diameter(tree)
        return self.diameter - 1


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

    diameter = Diameter()
    print(f"\n\nDiameter of the Tree: {diameter.get_diameter(btree)}")

    btree = BinaryTree(25)
    btree.insertion(20)
    btree.insertion(40)
    btree.insertion(15)
    btree.insertion(23)
    btree.insertion(35)
    btree.insertion(30)
    btree.insertion(21)

    print("\nInorder Traversal:")
    inorder_traversal(btree)

    diameter = Diameter()
    print(f"\n\nDiameter of the Tree: {diameter.get_diameter(btree)}")
