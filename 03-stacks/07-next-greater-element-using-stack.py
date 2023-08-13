# Finding the next greater element using nested loops first and then using stack
class Stack:
    def __init__(self):
        self.elements = []

        # output expression
        self.output = []

    def is_empty(self):
        return not self.elements

    def push(self, item):
        self.elements.append(item)
        # print(f"pushed {item}")

    def pop(self):
        if not self.is_empty():
            item = self.elements.pop()
            # print(f"popped {item}")
            return item

        print("can't pop. stack underflow!")

    def peek(self):
        if not self.is_empty():
            # print(f"Top element {self.elements[-1]}")
            return self.elements[-1]
        # print("stack underflow!")
        return


def next_greater_element_heuristic(array):
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


def next_greater_element_using_stack(array):
    stack = Stack()

    # push the first element to the stack
    stack.push(array[0])
    for i in range(1, len(array)):
        current_item = array[i]

        # until the elements in the stack are smaller
        # current element would be the NGE for them
        while (stack.peek()) and (stack.peek() < current_item):
            popped = stack.pop()
            print(f"{popped} -- {current_item}")

        stack.push(current_item)

    # for remaining elements in stack pair with 1
    while stack.peek():
        popped = stack.pop()
        print(f"{popped} -- -1")


if __name__ == "__main__":
    input_array = [4, 7, 9, 2, 16, 12, 18, 21, 19, 40, 40, 40]

    print(f"Input Array {input_array}")
    print("Using Nested Loops")
    next_greater_element_heuristic(input_array)

    print("\nUsing Stack")
    print(f"Input Array {input_array}")
    next_greater_element_using_stack(input_array)
