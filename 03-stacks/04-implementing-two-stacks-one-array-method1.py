# implementing two stacks in one array
# in this method we would divide the stack in two equal parts from the half.


class TwoStack:
    def __init__(self, size):
        self.size = size
        self.elements = [None] * self.size

        # defining the two tops
        self.top1 = self.size // 2
        self.top2 = (self.size // 2) - 1

    def push1(self, item):
        # there should be at least one space left
        if self.top1 > 0:
            # decreasing the first top one position left
            self.top1 -= 1

            # pushing the item
            self.elements[self.top1] = item
            print(f"pushed {item}")
        else:
            print(f"can't push {item}. Stack 1 overflow!")

    def push2(self, item):
        # if top2 is smaller than the size of the array
        if self.top2 < (self.size - 1):
            # increasing the top to one position ahead
            self.top2 += 1

            # pushing the element
            self.elements[self.top2] = item
            print(f"pushed {item}")
        else:
            print(f"can't push {item}. Stack 2 overflow!")

    def pop1(self):
        if self.top1 < self.size // 2:
            # popping the left most from the stack 1
            item = self.elements[self.top1]

            # increasing the top 1 to one position right
            self.top1 += 1

            return item
        else:
            print("Can't pop. Stack 1 underflow!")

    def pop2(self):
        if self.top2 > (self.size // 2) - 1:
            # popping the right most from the stack 2
            item = self.elements[self.top2]

            # increasing the top 1 to one position right
            self.top2 -= 1

            return item
        else:
            print("Can't pop. Stack 2 underflow!")

    def peek1(self):
        return self.elements[self.top1]

    def peek2(self):
        return self.elements[self.top2]


if __name__ == "__main__":
    twostack = TwoStack(7)

    twostack.push1(4)
    twostack.push1(3)
    twostack.push1(2)
    twostack.push1(1)
    twostack.push2(5)
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
    print(f"Top1: {twostack.peek1()}")
    print(f"Popped1: {twostack.pop1()}")
    print(f"Top1: {twostack.peek1()}")
    print(f"Popped1: {twostack.pop1()}")
