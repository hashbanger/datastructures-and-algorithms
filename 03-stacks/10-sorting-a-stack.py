# Sorting a given stack using recursion
# Here we use the same concept as in reversing stack using recursion but
# we just add another condition where we do not pick up the previous elements while inserting
# if they are smaller/greater than the one we want to push.
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

    def sort_stack(self):
        # until the stack is not empty
        if self.peek() is not None:
            # store the top element on the stack frame
            temp = self.pop()

            # recursively sort the remaining stack
            self.sort_stack()

            # insert the stored element to its sorted place
            self.sorted_insert(temp)

    def sorted_insert(self, item):
        # if the stack is not empty or top is smaller than the item then push
        if (self.peek() is None) or (self.peek() < item):
            self.push(item)

        # otherwise
        else:
            # store the top element
            temp = self.pop()

            # recursively insert the item
            self.sorted_insert(item)

            # push the stored element back
            self.push(temp)


if __name__ == "__main__":
    stack = Stack()
    stack.push(34)
    stack.push(12)
    stack.push(6)
    stack.push(88)

    print(f"Stack: {stack.elements}")
    stack.sort_stack()
    print(f"Sorted Stack: {stack.elements}")
