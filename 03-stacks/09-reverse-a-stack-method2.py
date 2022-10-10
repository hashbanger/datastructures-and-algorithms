# We will reverse the elements of the stack using recursion
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

        # until the stack is not empty
        if self.peek() is not None:

            # hold out the top in the recursion stack
            temp = self.pop()

            # recursively reverse the remaining stack
            self.reverse()

            # then insert the held out element at the bottom
            self.insert_at_bottom(temp)

    def insert_at_bottom(self, item):

        # if the stack is empty then push to stack
        if self.peek() is None:
            self.push(item)

        # if the stack is not empty then
        else:

            # hold out the top in the recursion stack
            temp = self.pop()

            # try to insert in the remaining stack
            self.insert_at_bottom(item)

            # push the held out item back
            self.push(temp)


if __name__ == "__main__":
    stack = Stack(10)

    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)

    print(f"Stack: {stack.elements}")
    stack.reverse_stack()
    print(f"Reversed Stack: {stack.elements}")
