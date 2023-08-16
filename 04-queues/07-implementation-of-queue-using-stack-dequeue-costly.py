# Implementing a queue using stacks with dequeue costly operation
# We enqueue normally in the stack but while dequeue we put all in second stack and pop
# then we put them back in the first stack.
class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()
            return item

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        return False


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
            return False

        self.stack1.push(item)

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return False

        while not self.stack1.is_empty():
            item = self.stack1.pop()
            self.stack2.push(item)

        popped = self.stack2.pop()

        while not self.stack2.is_empty():
            item = self.stack2.pop()
            self.stack1.push(item)

        return popped

    def peek(self):
        if self.is_empty():
            return False

        while not self.stack1.is_empty():
            item = self.stack1.pop()
            self.stack2.push(item)

        front = self.stack2.peek()

        while not self.stack2.is_empty():
            item = self.stack2.pop()
            self.stack1.push(item)

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
