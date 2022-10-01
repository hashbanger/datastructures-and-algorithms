# implementation of a stack using python
class ConversionStack:
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
        return self.elements[self.top]

    # to check whether the element is a operand or not
    def is_operand(self, ch):
        return ch.isdigit()

    def evaluate_postfix(self, expression):

        for ch in expression:

            # if the item is an operand we push it to stack
            if self.is_operand(ch):
                self.push(ch)

            # if we encounter an operator, we evaluate using last two operands
            # then push it to the stack
            else:
                value_2 = self.pop()
                value_1 = self.pop()
                self.push(str(eval(value_1 + ch + value_2)))

        return int(self.pop())


if __name__ == "__main__":
    postfix_expression = "231*+9-"
    print(f"Postfix Expression {postfix_expression}")

    conversion_stack = ConversionStack(size=len(postfix_expression))
    postfix_evaluation = conversion_stack.evaluate_postfix(postfix_expression)

    print(f"Evaluated Value {postfix_evaluation}")
