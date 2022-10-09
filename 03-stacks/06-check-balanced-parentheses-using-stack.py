# implementation of a stack using python
class BalanceStack:
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

    def check_balanced_parentheses(self, input_string):
        if not input_string:
            return True

        for ch in input_string:
            if ch in ["{", "(", "["]:
                self.push(ch)
            else:
                popped = self.pop()

                if (ch == "}") and (popped != "{"):
                    return False
                elif (ch == ")") and (popped != "("):
                    return False
                elif (ch == "]") and (popped != "["):
                    return False

        if self.peek():
            return False
        return True


if __name__ == "__main__":
    stk = BalanceStack(10)

    result = stk.check_balanced_parentheses("[]}[[[]]]")
    print(result)
