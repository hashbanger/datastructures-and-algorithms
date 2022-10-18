# implementing double ended queue using circular array
class Dequeue:
    def __init__(self, size):
        self.size = size
        self.elements = [None] * self.size
        self.front = -1
        self.rear = -1
        self.count = 0

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def insert_at_front(self, item):
        if self.is_full():
            print(f"Queue overflow by {item}")
            return

        if self.is_empty():
            self.rear = 0

        self.front -= 1

        # we move the front to the end of the array if it reaches negative index
        if self.front < 0:
            self.front = self.size - 1

        self.elements[self.front] = item
        self.count += 1

    def insert_at_rear(self, item):
        if self.is_full():
            print(f"Queue Overflow by {item}")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.elements[self.rear] = item
        self.count += 1

    def delete_from_front(self):
        if self.is_empty():
            print("Queue Underflow!")
            return

        item = self.elements[self.front]

        self.front = (self.front + 1) % self.size
        self.count -= 1

        return item

    def delete_from_rear(self):
        if self.is_empty():
            print("Queue Underflow!")
            return

        item = self.elements[self.rear]

        self.rear -= 1

        # we move rear to the end of the array if it reaches negative index
        if self.rear < 0:
            self.rear = self.size - 1

        self.count -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        print(f"Front element: {self.elements[self.front]}")
        return self.elements[self.front]

    def peek_rear(self):
        if self.is_empty():
            print("Queue Underflow")
            return
        print(f"Rear element: {self.elements[self.rear]}")
        return self.elements[self.rear]


if __name__ == "__main__":
    dequeue = Dequeue(5)
    dequeue.insert_at_rear(4)
    dequeue.insert_at_rear(2)
    dequeue.insert_at_rear(0)
    dequeue.insert_at_rear(1)
    dequeue.insert_at_rear(3)
    dequeue.insert_at_rear(5)

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.delete_from_front()

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.insert_at_front(6)

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.delete_from_rear()

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.insert_at_rear(5)

    dequeue.peek_front()
    dequeue.peek_rear()

    dequeue.delete_from_front()

    dequeue.peek_front()
    dequeue.peek_rear()
