# Sorting a given stack using recursion
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
        print("stack underflow!")
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
    stack = Stack(5)
    stack.push(34)
    stack.push(12)
    stack.push(6)
    stack.push(88)

    print(f"Stack: {stack.elements}")
    stack.sort_stack()
    print(f"Sorted Stack: {stack.elements}")
