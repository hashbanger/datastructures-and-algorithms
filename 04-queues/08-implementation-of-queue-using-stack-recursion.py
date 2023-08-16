# Implementing a queue using stacks using recursion
# We hold out the elements in recursion stack until the last element
# then we return back the last element and push back the hold out elements.
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
        self.stack = Stack(self.size)

    def get_size(self):
        return self.count

    def is_empty(self):
        return self.get_size() == 0

    def is_full(self):
        return self.get_size() == self.size

    def enqueue(self, item):
        if self.is_full():
            return False

        self.stack.push(item)

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return False

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
            return False

        top_element = self.stack.pop()

        # if it's the last element we print it and add it back
        if self.stack.is_empty():
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
