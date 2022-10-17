# Implementing a special stack that keeps track of the minimum value in the stack.

# We will use a simple stack for the second auxiliary stack that would be used in the Special stack.
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


class SpecialStack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.min_stack = Stack(self.size)
        self.elements = []

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.size - 1)

    def push(self, item):
        if not self.is_full():

            # adding the element to the stack
            self.elements.append(item)
            print(f"pushed {item}")

            # increasing the top to one position up
            self.top += 1

            # push if the stack is empty or if the item is smaller than current minimum
            if (self.min_stack.peek() is None) or (item <= self.min_stack.peek()):
                self.min_stack.push(item)

            # otherwise push the current minimum again
            else:
                self.min_stack.push(self.min_stack.peek())

        else:
            print("Can't push. Stack overflow!")
            return False

    def pop(self):
        if not self.is_empty():

            # popping the last element from the stacks
            item = self.elements.pop()
            min_item = self.min_stack.pop()
            print(f"popped {item}")

            self.top -= 1
            return item
        else:
            print("Can't pop. Stack underflow!")
            return False

    def get_min(self):
        print(f"minimum {self.min_stack.peek()}")
        return self.min_stack.peek()

    def peek(self):
        if not self.is_empty():
            print(f"Top element {self.elements[self.top]}")
            return self.elements[self.top]
        print("stack underflow!")
        return


if __name__ == "__main__":
    special_stack = SpecialStack(10)
    special_stack.push(8)
    special_stack.get_min()

    special_stack.push(4)
    special_stack.get_min()

    special_stack.push(14)
    special_stack.get_min()

    special_stack.push(45)
    special_stack.get_min()

    special_stack.push(3)
    special_stack.get_min()

    special_stack.push(-2)
    special_stack.get_min()

    special_stack.push(12)
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()
