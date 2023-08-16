# Implemented a queue using the traditional approach of manually moving front and rear.
# Also added a pythonic implementation which is more usable for problem solving.
class TraditionalQueue:
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
        print(f"enqueued {item}")

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
        print(f"dequeued {item}")

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


class Queue:
    def __init__(self):
        self.count = 0
        self.elements = []

    def get_size(self):
        return self.count

    def is_empty(self):
        return not self.elements

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return False

    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        return False


if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.enqueue(8)
    queue.enqueue(10)
    queue.enqueue(12)

    queue.dequeue()
    queue.dequeue()

    queue.peek()

    queue.enqueue(12)
    queue.enqueue(14)

    queue.peek()
