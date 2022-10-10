# reversing a string using stack
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

    def is_empty(self):
        return True if self.top == -1 else False

    def push(self, item):
        if self.top < self.size - 1:

            # adding the element to the stack
            self.elements.append(item)

            # increasing the top to one position up
            self.top += 1
        else:
            print("Can't push. Stack overflow!")

    def pop(self):
        if self.top != -1:

            # popping the last element from the stack
            item = self.elements.pop()

            # decreasing the top to one position down
            self.top -= 1
            return item
        else:
            print("Can't pop. Stack underflow!")

    def peek(self):
        if self.top == -1:
            return None
        return self.elements[self.top]


def reverse_string(input_string):
    stack = Stack(len(input_string))

    # first we push all the elements to the stack
    for ch in input_string:
        stack.push(ch)

    # empty the string, we would use it to store the results
    input_string = ""

    # popping the elements are adding them back to the string
    while stack.peek():
        input_string += stack.pop()

    return input_string


if __name__ == "__main__":
    input_string = "cogito ergo sum"
    print(f"Input String: {input_string}")

    reverse_string = reverse_string(input_string)
    print(f"Reverse String: {reverse_string}")
