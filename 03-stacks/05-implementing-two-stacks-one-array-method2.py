# implementing two stacks in one array
# in this method we would do dynamic implementation.


class TwoStack:
    def __init__(self, size):
        self.size = size
        self.elements = [None] * self.size

        # defining the two tops
        self.top1 = -1
        self.top2 = self.size

    def is_empty(self):
        return True if self.top == -1 else False

    def push1(self, item):

        # if there at least one space between the two tops
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.elements[self.top1] = item
        else:
            print(f"Stack 1 overflow by {item}!")

    def push2(self, item):

        # if there at least one space between the two tops
        if self.top2 - 1 > self.top1:  # (self.top1 + 1 < self.top2) also works
            self.top2 -= 1
            self.elements[self.top2] = item
        else:
            print(f"Stack 2 overflow by {item}!")

    def pop1(self):
        if self.top1 > -1:
            item = self.elements[self.top1]
            self.top1 -= 1

            return item
        else:
            print("Stack 1 underflow!")

    def pop2(self):
        if self.top2 < self.size:
            item = self.elements[self.top2]
            self.top2 += 1

            return item
        else:
            print("Stack 2 underflow!")

    def peek1(self):
        return self.elements[self.top1] if self.top1 > -1 else None

    def peek2(self):
        return self.elements[self.top2] if self.top2 < self.size else None


if __name__ == "__main__":
    twostack = TwoStack(7)

    twostack.push1(1)
    twostack.push1(2)
    twostack.push1(3)
    twostack.push1(4)
    twostack.push1(5)
    twostack.push2(6)
    twostack.push2(7)
    twostack.push2(8)
    twostack.push2(9)
    print(f"All elements: {twostack.elements}")
    print(f"Popped1: {twostack.pop1()}")
    print(f"Popped2: {twostack.pop2()}")
    print(f"Top1: {twostack.peek1()}")
    print(f"Top2: {twostack.peek2()}")

    print(f"Popped1: {twostack.pop1()}")
    print(f"Popped2: {twostack.pop2()}")
    print(f"Top1: {twostack.peek1()}")
    print(f"Top2: {twostack.peek2()}")
