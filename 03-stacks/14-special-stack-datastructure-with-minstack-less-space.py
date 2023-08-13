# Implementing a special stack that keeps track of the minimum value in the stack.
# We will use a simple stack for the second auxiliary stack that would be used in the Special stack.
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
        return


class SpecialStack:
    def __init__(self):
        self.min_stack = Stack()
        self.elements = []

    def is_empty(self):
        return not self.elements

    def push(self, item):
        # adding the element to the stack
        self.elements.append(item)

        # if the stack is empty then push to the stack
        if (self.min_stack.peek() is None) or (item <= self.min_stack.peek()):
            self.min_stack.push(item)

    def pop(self):
        if not self.is_empty():

            # popping the last element from the stacks
            item = self.elements.pop()

            # if the popped item is the same as current min then pop it
            if item == self.min_stack.peek():
                min_item = self.min_stack.pop()

        else:
            return False

    def get_min(self):
        return self.min_stack.peek()

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        return


if __name__ == "__main__":
    special_stack = SpecialStack()
    special_stack.push(8)
    print(special_stack.get_min())

    special_stack.push(4)
    print(special_stack.get_min())

    special_stack.push(14)
    print(special_stack.get_min())

    special_stack.push(45)
    print(special_stack.get_min())

    special_stack.push(3)
    print(special_stack.get_min())

    special_stack.push(-2)
    print(special_stack.get_min())

    special_stack.push(12)
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())
