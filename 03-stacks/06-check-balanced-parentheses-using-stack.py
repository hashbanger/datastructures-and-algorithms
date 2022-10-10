# checking for balanced parenthese in a string using stack
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


def check_balanced_parentheses(input_string):
    # initializing the stack to use
    stack = Stack(10)

    if not input_string:
        return True

    for ch in input_string:
        if ch in ["{", "(", "["]:
            stack.push(ch)
        else:
            popped = stack.pop()

            if (ch == "}") and (popped != "{"):
                return False
            elif (ch == ")") and (popped != "("):
                return False
            elif (ch == "]") and (popped != "["):
                return False

    if stack.peek():
        return False
    return True


if __name__ == "__main__":
    input_string = "[]{}((([[[]]])))"
    result = check_balanced_parentheses(input_string)
    print(f"Input String {input_string}")
    print(f"Result {result}")

    input_string = "[]}[[[]]]"
    result = check_balanced_parentheses(input_string)
    print(f"Input String {input_string}")
    print(f"Result {result}")
