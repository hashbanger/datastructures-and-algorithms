# Implementing a special stack that keeps track of the minimum value in the stack.

# We will do the operation in O(1) space complexity, without using a second stack.
class SpecialStack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []
        self.min = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.size - 1)

    def push(self, item):
        if not self.is_full():

            # if the stack is empty we just push the values to the stack
            if self.peek() is None:
                self.min = item
                self.elements.append(item)

            # if the current value is smaller than minimum
            elif item < self.min:

                # then we push a dummy value calculated using the formula, (2 * item - current_min), setting new_min = item
                self.elements.append((2 * item) - self.min)
                self.min = item
            else:
                self.elements.append(item)

            self.top += 1
            print(f"pushed {item}")

        else:
            print("Can't push. Stack overflow!")
            return False

    def pop(self):
        if not self.is_empty():

            # popping the last element from the stacks
            item = self.elements.pop()
            actual_popped = item

            # if the current item is smaller than current minimum means it is the dummy value for the current minimum
            if item < self.min:
                actual_popped = self.min

                # since we calculated the dummy value for the minimum using (2 * value - prev_min), new_min = value
                # to get the previous minimum we can subtract it from twice the (new_min=value)
                # 2 * value - (2 * value - prev_min) = prev_min
                self.min = 2 * self.min - item

            self.top -= 1
            print(f"popped {actual_popped}")
            return actual_popped

        else:
            print("Can't pop. Stack underflow!")
            return False

    def get_min(self):
        if self.peek() is None:
            print(f"minimum {None}")
            return None
        print(f"minimum {self.min}")
        return self.min

    def peek(self):
        if not self.is_empty():
            print(f"Top element {self.elements[self.top]}")
            return self.elements[self.top]
        print("stack underflow!")
        return


if __name__ == "__main__":
    special_stack = SpecialStack(10)
    special_stack.push(8)
    special_stack.get_min()

    special_stack.push(4)
    special_stack.get_min()

    special_stack.push(14)
    special_stack.get_min()

    special_stack.push(45)
    special_stack.get_min()

    special_stack.push(3)
    special_stack.get_min()

    special_stack.push(-2)
    special_stack.get_min()

    special_stack.push(12)
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()

    special_stack.pop()
    special_stack.get_min()
