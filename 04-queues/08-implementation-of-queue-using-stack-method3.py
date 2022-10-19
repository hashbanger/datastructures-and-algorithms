# implementing a queue using stacks using recursion
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
        self.stack = Stack(self.size)

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

        self.stack.push(item)

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        top_element = self.stack.pop()

        # if it is the last element
        # we return the element
        if self.stack.is_empty():

            self.count -= 1
            return top_element

        item = self.dequeue()

        # add the removed element back if it's not last
        self.stack.push(top_element)

        return item

    def peek(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        top_element = self.stack.pop()

        # if it's the last element we print it and add it back
        if self.stack.is_empty():
            print(f"Front {top_element}")
            self.stack.push(top_element)

            return top_element

        item = self.peek()

        self.stack.push(top_element)

        return item


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

    queue.peek()

    queue.dequeue()

    queue.peek()
