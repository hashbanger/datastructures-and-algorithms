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


def stock_span_solve_brute(array):

    # initialize the empty array to store the spans
    spans = [None] * len(array)

    # initialize the first span
    spans[0] = 1

    # we will iterate through each element and
    # move backwards from that index while checking the number
    for i in range(len(array)):
        spans[i] = 1

        # moving backwards
        j = i - 1

        # if the array is not exhausted and value is smaller than current
        while (j >= 0) and (array[j] < array[i]):

            # increase the span
            spans[i] += 1

            # move back another step
            j -= 1

    return spans


def stock_span_solve_stack(array):
    stack = Stack(len(array))
    spans = []

    # iterate through the array
    for i in range(len(array)):

        price = array[i]
        days = 1

        # if the stack is not empty and the price on the top is smaller then
        while (stack.peek() is not None) and (stack.peek()[0] <= price):

            # pop the elements and
            popped = stack.pop()
            spans.append(popped)

            # add its days to current days
            days += popped[1]

        # push the new pair to the stack
        stack.push([price, days])

    # empty the remaining elements
    while stack.peek() is not None:
        spans.append(stack.pop())

    return spans


if __name__ == "__main__":
    input_array = [10, 4, 5, 90, 120, 80]
    result_span = stock_span_solve_brute(input_array)
    print(f"Input Array: {input_array}")
    print(f"Stock Span: {result_span}")

    result_span = stock_span_solve_stack(input_array)
    print(f"Input Array: {input_array}")
    print(f"Stock Span: {result_span}")
