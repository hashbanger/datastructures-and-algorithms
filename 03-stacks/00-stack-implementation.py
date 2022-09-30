# implementation of a stack using python
class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

    def is_empty(self):
        return 1 if self.top == -1 else False

    def push(self, item):
        if self.top < self.size - 1:

            # adding the element to the stack
            self.elements.append(item)
            print(f"pushed {item}")

            # increasing the top to one position up
            self.top += 1
        else:
            print("Can't push. Stack overflow!")

    def pop(self):
        if self.top != -1:

            # popping the last element from the stack
            item = self.elements.pop()
            print(f"popped {item}")

            # decreasing the top to one position down
            self.top -= 1
            return item
        else:
            print("Can't pop. Stack underflow!")

    def peek(self):
        print(f"Top element {self.elements[self.top]}")


if __name__ == "__main__":
    stk = Stack(5)
    stk.push(5)
    stk.push(4)
    stk.push(3)
    stk.push(2)
    stk.push(1)
    stk.push(2)

    stk.peek()

    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
