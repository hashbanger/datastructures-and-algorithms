# We will reverse the elements of the stack using a second stack
class Stack:
    def __init__(self):
        self.elements = []
        self.output = []

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
        return

    def reverse(self):
        new_stack = Stack()

        # until the stack is empty pop the element and push to second stack
        while self.peek() is not None:
            new_stack.push(self.pop())

        # return the new stack
        self.elements = new_stack.elements


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)

    print(f"Stack: {stack.elements}")
    stack.reverse()
    print(f"Reversed Stack: {stack.elements}")
