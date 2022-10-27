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

    def inorder_traversal(self):
        if self.data:

            # if not none, recursively iterate in the left direction
            if self.left:
                self.left.inorder_traversal()

            # output the root value
            print(self.data, end=" ")

            # if not none, recursively iterate in the right direction
            if self.right:
                self.right.inorder_traversal()

    def traverse_current_level(self, level):

        # level decreases recursively until final desired level is reached
        if level == 1:
            print(self.data, end=" ")

        # if not reached to the level go one level below each side
        elif level > 1:

            # if left exisits recursively iterate to next level
            if self.left:
                self.left.traverse_current_level(level - 1)

            # if right exisits recursively iterate to next level
            if self.right:
                self.right.traverse_current_level(level - 1)

    def get_height(self):
        left_height = right_height = -1

        # if there is left child then recursively obtain it's height
        if self.left:
            left_height = self.left.get_height()

        # if there is right child then recrusively obtain it's height
        if self.right:
            right_height = self.right.get_height()

        # the larger one would be considered the height at the current node
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def breadth_first_traversal(self):

        # get the height for the tree
        height = self.get_height()

        # for each level traverse all the level nodes
        for h in range(1, height + 1):
            self.traverse_current_level(h)
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
    btree.inorder_traversal()

    print("\n\nBreadth First Traversal:")
    btree.breadth_first_traversal()
