# connecting the nodes that are at the same level in the tree
class Queue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.count = 0
        self.elements = [None] * self.size

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue Overflow by {item}")
            return

        # if its is the first item then we initialize the front to the first spot
        if self.front == -1:
            self.front = 0

        # increase the rear by one position (make it capable to circle back to empty places)
        self.rear = (self.rear + 1) % self.size

        # then insert the item at the new rear position
        self.elements[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print(f"Queue Underflow!")
            return

        # get the front element
        item = self.elements[self.front]

        # increase the front to the next inserted element (make it capable to circle back)
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item

    def peek(self):
        if not self.is_empty():
            print(f"front element {self.elements[self.front]}")
            return self.elements[self.front]

        print("Queue Underflow!")
        return


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


# def breadth_first_traversal_(tree):
#     if tree is None:
#         return

#     # create a queue and enqueue the first element
#     queue = Queue(50)
#     queue.enqueue(tree)

#     # until the queue is empty
#     while not queue.is_empty():

#         level_count = queue.get_size()

#         for i in range(level_count):
#             # remove the first element and print it
#             item = queue.dequeue()

#             # enque its children nodes if they exist
#             if item.left:
#                 queue.enqueue(item.left)
#             if item.right:
#                 queue.enqueue(item.right)

#             if item.next_right:
#                 print(f"{item.data}", end=" -> ")
#             else:
#                 print(f"{item.data}", end=" ")

#         print()


def connect_level_nodes(tree):
    if tree is None:
        return

    # create a queue and enqueue the first element
    queue = Queue(50)
    queue.enqueue(tree)

    prev = BinaryTree(None)

    # until the queue is empty
    while not queue.is_empty():

        # getting the count of number of nodes at current level
        level_count = queue.get_size()

        for i in range(level_count):

            # remove the first element and print it
            item = queue.dequeue()

            # enque its children nodes if they exist
            if item.left:
                queue.enqueue(item.left)
            if item.right:
                queue.enqueue(item.right)

            # if not leftmost then assign the current as the next right of the previous
            if i > 0:
                prev.next_right = item

            # assigning current node as new previous
            prev = item

        # assigning right as None for the right most node at a level
        prev.next_right = None


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
    # breadth_first_traversal(btree)

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
    # breadth_first_traversal(btree)
