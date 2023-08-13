# We will reverse the elements of the stack using recursion
# First take the elements one by one and hold them like in a hand using recursion stack,
# then insert the last picked out element into the stack when the stack is empty.
# Then before putting the next in line element, pick up in hand the ones already pushed again using recursion stack
# and insert the current in the bottom.

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
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(f"Stack: {stack.elements}")
    stack.reverse()
    print(f"Reversed Stack: {stack.elements}")
