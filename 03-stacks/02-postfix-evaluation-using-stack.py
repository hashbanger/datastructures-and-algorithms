# evaluating a postfix expression uisnga stack
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

    def perform_operation(self, operand1, operand2, operator):
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        elif operator == "^":
            return operand1**operand2
        else:
            print(f"Invalid operator: {operator}")

    # to check whether the element is a operand or operator
    def is_operand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def evaluate_postfix(self, expression):
        for ch in expression:
            # if the item is an operand we push it to stack
            if self.is_operand(ch):
                self.push(ch)

            # if we encounter an operator, we evaluate using last two operands
            # then push it to the stack
            else:
                value_2 = int(self.pop())
                value_1 = int(self.pop())
                result = self.perform_operation(value_1, value_2, ch)
                self.push(result)

        return self.pop()


if __name__ == "__main__":
    # postfix_expression = "231*+9-"
    postfix_expression = "342+*15-2^/"
    print(f"Postfix Expression {postfix_expression}")

    conversion_stack = ConversionStack()
    postfix_evaluation = conversion_stack.evaluate_postfix(postfix_expression)

    print(f"Evaluated Value {postfix_evaluation}")
