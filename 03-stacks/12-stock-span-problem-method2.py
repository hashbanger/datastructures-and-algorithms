# Solving the stock span problem using brute force and then stack
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.size - 1)

    def push(self, item):
        if not self.is_full():

            # adding the element to the stack
            self.elements.append(item)

            # increasing the top to one position up
            self.top += 1
        else:
            return False

    def pop(self):
        if not self.is_empty():

            # popping the last element from the stack
            item = self.elements.pop()

            # decreasing the top to one position down
            self.top -= 1
            return item
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.elements[self.top]
        print("stack underflow!")
        return


def stock_span_solve_stack(array):
    stack = Stack(len(array))
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
