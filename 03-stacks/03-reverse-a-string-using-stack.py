# reversing a string using stack
class Stack:
    def __init__(self):
        self.elements = []
        self.output = []

    def is_empty(self):
        return not self.elements

    def push(self, item):
        self.elements.append(item)
        print(f"pushed {item}")

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()
            print(f"popped {item}")
            return item

        print("can't pop. stack underflow!")

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        print("stack underflow!")
        return


def reverse_string(input_string):
    stack = Stack()

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
