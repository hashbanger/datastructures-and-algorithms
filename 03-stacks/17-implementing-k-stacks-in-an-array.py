# Implementing K different stacks in an array
# We will be using space efficient method and making the entire process dynamic with the use of two additional integer arrays
# Here'a reference video to understand the working better. (https://www.youtube.com/watch?v=UmyOXVIjUoI&t=847s)
class KStacks:
    def __init__(self, nstacks, size):
        self.size = size
        self.nstacks = nstacks
        self.elements = [None] * size

        # to maintain the top of each stacks
        self.tops = [-1] * nstacks

        # to get the immediate next free spot
        self.free = 0

        # to track free spots and chain of tops for the stacks
        self.nexts = [i + 1 for i in range(size)]
        self.nexts[self.size - 1] = -1

    def is_empty(self, stack_num):
        return self.tops[stack_num] == -1

    def is_full(self):
        return self.free == -1

    def push(self, item, stack_num):
        if self.is_full():
            print(f"Stack Overflow by {item}")
            return

        # get the current free index
        insert_at = self.free

        # next free spot index would be the one that is pointed by the current free spot
        self.free = self.nexts[insert_at]

        # we store the current top of the stack (before insertion) into the current free spot index
        self.nexts[insert_at] = self.tops[stack_num]

        # updating the top
        self.tops[stack_num] = insert_at

        # pushing the element into the array
        self.elements[insert_at] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            print("Stack Underflow!")
            return None

        # getting the current top of the corresponding stack
        stack_top = self.tops[stack_num]

        # we update the top of the stack with the last top that we have stored
        self.tops[stack_num] = self.nexts[stack_top]

        # as the current spot is now free we link it prior to the next free spot
        self.nexts[stack_top] = self.free

        # updating the immediate free spot as the current one
        self.free = stack_top

        print(f"popped {self.elements[stack_top]}")
        return self.elements[stack_top]

    def peek(self, stack_num):
        if not self.is_empty(stack_num):
            stack_top = self.tops[stack_num]
            return self.elements[stack_top]

        print("Stack underflow! No peek.")
        return None

    def peek_all(self, stack_num):
        if not self.is_empty(stack_num):
            ptr = self.tops[stack_num]
            while ptr != -1:
                print(self.elements[ptr], end="-")
                ptr = self.nexts[ptr]
            print()
            return

        print("Stack Underflow!")
        return


if __name__ == "__main__":
    kstacks = KStacks(3, 10)

    # pushing onto third stack
    kstacks.push(15, 2)
    kstacks.push(45, 2)

    # pushing onto the second stack
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)

    # pushing on the first stack
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    # printing all stacks
    kstacks.peek_all(0)
    kstacks.peek_all(1)
    kstacks.peek_all(2)

    # popping from the stacks
    kstacks.pop(2)
    kstacks.pop(2)
    kstacks.pop(0)
    kstacks.pop(1)

    # printing all stacks
    kstacks.peek_all(0)
    kstacks.peek_all(1)
    kstacks.peek_all(2)
