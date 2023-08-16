# Generating binary numbers 1 to N using a queue.
# The idea is very simple, if you start with 1 and enqueue it,
# then at each iteration you remove from the queue and enqueue the same element once with added 0 and once with added 1.
# 1 --> (10, 11),  10 --> (100, 101), 11 --> (110, 111)...
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


def generate_binary_numbers(N):
    queue = Queue(N + 1)

    queue.enqueue("1")
    for _ in range(N):
        front = queue.dequeue()
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")

        print(front)


if __name__ == "__main__":
    generate_binary_numbers(100)
