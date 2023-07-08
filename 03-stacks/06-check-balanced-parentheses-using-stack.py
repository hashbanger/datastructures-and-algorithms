# checking for balanced parenthese in a string using stack
class Stack:
    def __init__(self):
        self.elements = []

        # output expression
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
            print(f"Top element {self.elements[-1]}")
            return self.elements[-1]
        print("stack underflow!")
        return


def check_balanced_parentheses(input_string):
    # initializing the stack to use
    stack = Stack()

    if not input_string:
        return True

    for ch in input_string:
        if ch in ["{", "(", "["]:
            stack.push(ch)
        elif ch in ["}", ")", "]"]:
            popped = stack.pop()

            if (ch == "}") and (popped != "{"):
                return False
            elif (ch == ")") and (popped != "("):
                return False
            elif (ch == "]") and (popped != "["):
                return False
        else:
            continue

    if stack.peek() is not None:
        return False
    return True


if __name__ == "__main__":
    input_string = "[]{}((([[[]]])))"
    result = check_balanced_parentheses(input_string)
    print(f"\nInput String {input_string}")
    print(f"Result {result}\n")

    input_string = "[]}[[[]]]"
    result = check_balanced_parentheses(input_string)
    print(f"\nInput String {input_string}")
    print(f"Result {result}\n")

    input_string = "3*(2+2) - (4*(6+2*(18/3))"
    result = check_balanced_parentheses(input_string)
    print(f"\nInput String {input_string}")
    print(f"Result {result}\n")
