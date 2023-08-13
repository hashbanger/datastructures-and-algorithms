# Implementing a special stack that keeps track of the minimum value in the stack.
# We will use a simple stack for the second auxiliary stack that would be used in the Special stack.
# Here we wouldn't push the same min element multiple times if the current is not smaller than current min
# then also while popping we wouldn't pop until the current element popped the the same current min in stack.
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

        # push if the stack is empty or if the item is smaller than current minimum
        if (self.min_stack.peek() is None) or (item <= self.min_stack.peek()):
            self.min_stack.push(item)

        # otherwise push the current minimum again
        else:
            self.min_stack.push(self.min_stack.peek())

    def pop(self):
        if not self.is_empty():
            # popping the last element from the stacks
            item = self.elements.pop()
            min_item = self.min_stack.pop()

            return item
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
