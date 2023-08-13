# Implementing a special stack that keeps track of the minimum value in the stack.
# We will do the operation in O(1) space complexity, without using a second stack.
# For this we when storing the mininmum, we overwrite the min value but 
# rather than pushing the same element in the stack we push a modified value using a formula that makes it smaller than the new min value value
# so while popping we would identify that if the stack element is smaller than min then its is the actual min that was pushed.
# and we would reverse the formula to get back previous minimum value.
class SpecialStack:
    def __init__(self):
        self.elements = []
        self.min = -1

    def is_empty(self):
        return not self.elements

    def push(self, item):
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
                self.min = 2 * actual_popped - item

            return actual_popped

        else:
            return False

    def get_min(self):
        if self.peek() is None:
            return None
        return self.min

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]
        return


if __name__ == "__main__":
    special_stack = SpecialStack()
    special_stack.push(8)
    print(special_stack.get_min())

    special_stack.push(4)
    print(special_stack.get_min())

    special_stack.push(14)
    print(special_stack.get_min())

    special_stack.push(45)
    print(special_stack.get_min())

    special_stack.push(3)
    print(special_stack.get_min())

    special_stack.push(-2)
    print(special_stack.get_min())

    special_stack.push(12)
    print(special_stack.get_min())

    print()    
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())

    special_stack.pop()
    print(special_stack.get_min())
