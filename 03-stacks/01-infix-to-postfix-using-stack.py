# converting an infix expression to postfix using a stack
class ConversionStack:
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

    # to check whether the element is a operand or operator
    def is_operand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def precedence(self, ch):
        precedence_values = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0}

        if ch not in precedence_values.keys():
            raise KeyError(f"operator {ch} not supported!")

        return precedence_values[ch]

    def infix_to_postfix(self, expression):
        for ch in expression:
            # Case1: add the output if it's an operand
            if self.is_operand(ch):
                self.output.append(ch)

            # Case 2: if it's an opening parentheses then push to stack
            elif ch == "(":
                self.push(ch)

            # Case 3: if it's a closing parentheses then
            elif ch == ")":
                # keep popping and add to output
                # until we find an opening parenthese or stack is empty
                while (not self.is_empty()) and (self.peek() != "("):
                    self.output.append(self.pop())

                if (not self.is_empty()) and (self.peek() != "("):
                    return -1

                # if we find an opening parenthese then just pop it away
                else:
                    self.pop()

            # Case 5: if it's an operator
            else:
                # keep popping operators and add to output till
                # current's precedence is not greater than top one in stack
                # or the stack runs empty
                while (not self.is_empty()) and (
                    self.precedence(ch) <= self.precedence(self.peek())
                ):
                    self.output.append(self.pop())

                # if precedence is greater then just push to the stack
                self.push(ch)

        # if we run out of characters in the expression
        # then just pop and add remaining operators if any in the stack
        while not self.is_empty():
            self.output.append(self.pop())

        return "".join(self.output)


if __name__ == "__main__":
    # infix_expression = "3*(4+2)/(1-5)^2"
    infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
    # infix_expression = "(7+3*(10/(12/(3+1)-1)))*(4-2)/(2+(3-1)*(2+2))"

    print(f"Infix Expression {infix_expression}")

    conversion_stack = ConversionStack()
    postfix_expression = conversion_stack.infix_to_postfix(infix_expression)

    print(f"Postfix Expression {postfix_expression}")
