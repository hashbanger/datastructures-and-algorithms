# implementation of a stack using python
class TraditionalStack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.elements = []

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if not self.is_full():

            # adding the element to the stack
            self.elements.append(item)
            print(f"pushed {item}")

            # increasing the top to one position up
            self.top += 1
        else:
            print("can't push. stack overflow!")

    def pop(self):
        if not self.is_empty():

            # popping the last element from the stack
            item = self.elements.pop()
            print(f"popped {item}")

            # decreasing the top to one position down
            self.top -= 1
            return item

        print("can't pop. stack underflow!")
        return

    def peek(self):
        if not self.is_empty():
            print(f"Top element {self.elements[self.top]}")
            return self.elements[self.top]
        print("stack underflow!")
        return

class Stack:
    def __init__(self, size):
        self.elements = []

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
    stk.pop()
