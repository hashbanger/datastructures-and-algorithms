# Finding the next greater element using nested loops first and then using stack
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


def next_greater_element_method1(array):

    # using nested loops
    # we will generate all pairs of next greatest elements
    for i in range(len(array)):
        item = array[i]
        next_max = -1
        for j in range(i + 1, len(array)):

            # update maximum if the item is smaller
            if item < array[j]:
                next_max = array[j]
                break
        print(f"{item} -- {next_max}")


def next_greater_element_method2(array):
    stack = Stack(len(array))

    element = 0
    next_item = 0

    # push one element to the stack initially
    stack.push(array[0])

    # until we have no next elements iterate
    for i in range(1, len(array)):
        next_item = array[i]

        # if the stack is not empty then
        if stack.peek() is not None:

            # pop one element from the stack
            element = stack.pop()

            # if the next item is greater then popped element then
            # keep popping and printing the pairs
            while next_item > element:
                print(f"{element} -- {next_item}")
                if stack.peek() is None:
                    break
                element = stack.pop()

            # if the next is smaller push the element back to the stack
            if next_item < element:
                stack.push(element)

        # push the next element to the stack
        stack.push(next_item)

    # if the stack is not empty then pop all and pair with -1
    while stack.peek() is not None:
        element = stack.pop()
        next_item = -1
        print(f"{element} -- {next_item}")


if __name__ == "__main__":
    input_array = [11, 13, 21, 3, 43]

    print(f"Input Array {input_array}")
    print("Using Nested Loops")
    next_greater_element_method1(input_array)

    print("\nUsing Stack")
    print(f"Input Array {input_array}")
    next_greater_element_method2(input_array)
