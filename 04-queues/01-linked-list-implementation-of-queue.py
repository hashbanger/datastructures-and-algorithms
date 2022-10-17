# Implementing a queue using a linked list approach
class Node:
    # a function to initialize the node object
    def __init__(self, data):
        self.data = data  # the assigned data
        self.next = None  # the next node


class Queue:
    def __init__(self, size):
        self.size = size
        self.front = None
        self.rear = None
        self.count = 0

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def enqueue(self, item):

        # we add node towards the rear
        if self.is_full():
            print(f"Queue Overflow by {item}")
            return

        new_node = Node(item)

        if self.rear == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def dequeue(self):

        # we remove a node from the front
        if self.is_empty():
            print("Queue Underflow!")
            return

        item = self.front
        self.front = item.next

        if self.front == None:
            self.rear = None

        self.count -= 1

    def peek(self):
        if self.is_empty():
            print("Queue Underflow!")
            return
        print(f"Front element {self.front.data}")


if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)
    queue.enqueue(10)
    queue.enqueue(12)
    queue.peek()

    queue.dequeue()
    queue.dequeue()

    queue.peek()

    queue.enqueue(12)
    queue.enqueue(14)

    queue.peek()
