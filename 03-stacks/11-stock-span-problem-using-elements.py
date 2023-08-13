# Solving the stock span problem using brute force and then stack
# For empty stack we push the first element with 1 span
# then for each element we pop the smaller stack elements and add their days to current span and push
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

def stock_span_solve_brute_using_for_loops_only(array):

    # initialize empty spans
    spans = [None] * len(array)

    for i in range(len(array)):
        spans[i] = 1
        
        # move backwards till end of array
        for j in range(i-1, -1, -1):
            if array[j] > array[i]:
                break

            # while elements are smaller keep adding to span
            spans[i] += 1

    return spans

def stock_span_solve_stack(array):
    stack = Stack()
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

    result_span = stock_span_solve_brute_using_for_loops_only(input_array)
    print(f"Input Array: {input_array}")
    print(f"Stock Span: {result_span}")

    result_span = stock_span_solve_stack(input_array)
    print(f"Input Array: {input_array}")
    print(f"Stock Span: {result_span}")
