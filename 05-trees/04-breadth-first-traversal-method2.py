# traversing the tree in a breadth first method, all nodes of the same level first. Using a Queue.
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

    def breadth_first_traversal(self):
        queue = Queue(50)

        temp_node = self
        queue.enqueue(temp_node)
        while not queue.is_empty():
            item = queue.dequeue()

            if item.left:
                queue.enqueue(item.left)

            if item.right:
                queue.enqueue(item.right)

            print(f"{item.data}", end=" ")


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
