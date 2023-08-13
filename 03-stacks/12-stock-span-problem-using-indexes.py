# Solving the stock span problem using brute force and then stack
# We begin pushing the first index in the stack
# then onwards we pop the smaller/equal element indexes
# if stack get empty, span would be current + 1 
# otherwise it would be current index - top index in stack
# and we push the current index.
class Stack:
    def __init__(self):
        self.elements = []
        self.output = []

    def is_empty(self):
        return not self.elements

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()
            return item

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        return


def stock_span_solve_stack(array):
    stack = Stack()
    spans = [None] * len(array)

    stack.push(0)

    # iterate through the array
    for i in range(len(array)):

        price = array[i]

        # if the stack is not empty and the price on the top is smaller then
        while (stack.peek() is not None) and (array[stack.peek()] <= price):
            stack.pop()

        if stack.peek() is None:
            spans[i] = i + 1
        else:
            spans[i] = i - stack.peek()

        stack.push(i)

    return spans


if __name__ == "__main__":
    input_array = [10, 4, 5, 90, 120, 80]
    result_span = stock_span_solve_stack(input_array)
    print(f"Input Array: {input_array}")
    print(f"Stock Span: {result_span}")
