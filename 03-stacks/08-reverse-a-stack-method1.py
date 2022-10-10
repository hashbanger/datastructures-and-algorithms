# We will reverse the elements of the stack using a second stack
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

    def is_empty(self):
        return 1 if self.top == -1 else False

    def push(self, item):
        if self.top < self.size - 1:

            # adding the element to the stack
            self.elements.append(item)

            # increasing the top to one position up
            self.top += 1
        else:
            return False

    def pop(self):
        if self.top != -1:

            # popping the last element from the stack
            item = self.elements.pop()

            # decreasing the top to one position down
            self.top -= 1
            return item
        else:
            return False

    def peek(self):
        if self.top == -1:
            return None
        return self.elements[self.top]

    def reverse(self):
        new_stack = Stack(10)

        # until the stack is empty pop the element and push to second stack
        while self.peek() is not None:
            new_stack.push(self.pop())

        # return the new stack
        self.elements = new_stack.elements


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)

    print(f"Stack: {stack.elements}")
    stack.reverse()
    print(f"Reversed Stack: {stack.elements}")
