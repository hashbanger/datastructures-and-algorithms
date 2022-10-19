# implementing a queue using stacks with enqueue costly operation
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.size - 1)

    def push(self, item):
        if not self.is_full():

            # adding the element to the stack
            self.elements.append(item)

            # increasing the top to one position up
            self.top += 1
        else:
            return False

    def pop(self):
        if not self.is_empty():

            # popping the last element from the stack
            item = self.elements.pop()

            # decreasing the top to one position down
            self.top -= 1
            return item
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.elements[self.top]
        return


class Queue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.stack1 = Stack(self.size)
        self.stack2 = Stack(self.size)

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

        while not self.stack1.is_empty():
            popped = self.stack1.pop()
            self.stack2.push(popped)

        self.stack1.push(item)

        while not self.stack2.is_empty():
            popped = self.stack2.pop()
            self.stack1.push(popped)

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        popped = self.stack1.pop()

        return popped

    def peek(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        front = self.stack1.elements[-1]

        print(f"Front: {front}")
        return front


if __name__ == "__main__":
    queue = Queue(10)
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)

    queue.peek()

    queue.dequeue()

    queue.peek()

    queue.dequeue()

    queue.peek()

    queue.enqueue(6)

    queue.dequeue()

    queue.peek()
