# converting an infix expression to postfix using a stack
class ConversionStack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

        # precedence settings
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        # output expression
        self.output = []

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

    # to check whether the element is a operand or operator
    def is_operand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def input_precedence_greater(self, opr):

        # first to compare if the next operator in the expression
        # has higher precedence or not
        try:
            input_precedence = self.precedence[opr]
            top_precedence = self.precedence[self.peek()]

            if input_precedence > top_precedence:
                return True
            else:
                return False

        # this is to consider an operator precedence greater then a bracket
        except KeyError:
            return True

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
                while (not self.is_empty()) and (not self.input_precedence_greater(ch)):
                    self.output.append(self.pop())

                # if precedence is greater then just push to the stack
                self.push(ch)

        # if we run out of characters in the expression
        # then just pop and add remaining operators if any in the stack
        while not self.is_empty():
            self.output.append(self.pop())

        return "".join(self.output)


if __name__ == "__main__":
    infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
    # infix_expression = "2*(2+3)+4"

    print(f"Infix Expression {infix_expression}")

    conversion_stack = ConversionStack(size=len(infix_expression))
    postfix_expression = conversion_stack.infix_to_postfix(infix_expression)

    print(f"Postfix Expression {postfix_expression}")
