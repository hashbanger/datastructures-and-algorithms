# We want to implement a stack that supports the following operations in O(N) complexity.
# push, pop, find the middle element, delete the middle element.
# We will use a doubly linked list to implement this stack.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.middle = None

    def insert_at_front(self, new_data, count):

        # creating new node
        new_node = Node(new_data)

        # creating connections
        new_node.next = self.head

        # if head is not none
        if self.head != None:
            self.head.prev = new_node

        # updating the count of nodes
        count += 1

        # if there is only one node, set it to middle
        if count == 1:
            self.middle = new_node

        # if the number of nodes is even we select n % 2 = q as the middle
        # if the number of nodes turns odd we select q+1 the prev (just above in stack as the new middle)
        else:
            if count % 2 != 0:
                self.middle = self.middle.prev

        # changing the head
        self.head = new_node

    def delete_node(self, dele, count):
        ptr = self.head

        # if the node to be deleted is the first node
        if ptr.data == dele.data:

            # if it is the last node, empty the list
            if count == 1:
                self.head = None

            # otherwise make next node as the head
            else:
                ptr.next.prev = None
                self.head = ptr.next

        # if the node to be deleted is middle (delete middle scenario)
        elif self.middle.data == dele.data:

            # make connections between adjacent nodes of middle
            self.middle.prev.next = self.middle.next
            self.middle.next.prev = self.middle.prev

        # decrease the node count
        count -= 1

        # if there are no nodes, set middle to none
        if count == 0:
            self.middle = None

        # if the nodes turn even, assign next (lower in stack) node as the middle
        elif count % 2 == 0:
            self.middle = self.middle.next

        return ptr.data

    def get_middle_node(self):
        if self.head is not None:
            return self.middle.data
        return None

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" - ")
            ptr = ptr.next
        print()


class MiddleStack:
    def __init__(self, size):
        self.size = size
        self.top_count = -1
        self.elements = LinkedList()

    def push(self, item):
        if self.top_count < self.size:
            print(f"pushed {item}")

            # we push the values to the front of the linked list
            self.elements.insert_at_front(new_data=item, count=self.top_count + 1)

            # increase the node count in the stack
            self.top_count += 1
        else:
            print(f"Stack overflow by {item}")
            return None

    def pop(self):
        if self.top_count > -1:

            # we delete the node from the front of the linked list
            item = self.elements.delete_node(
                dele=self.elements.head, count=self.top_count + 1
            )
            print(f"popped {item}")

            # reducing the node count in the stack
            self.top_count -= 1
        else:
            print(f"Stack underflow!")

    def get_middle(self):
        if self.top_count > -1:
            print(f"\nMiddle element in stack {self.elements.get_middle_node()}")

            # get the middle node from the linked list
            return self.elements.get_middle_node()

        print("Stack underflow! No middle.")
        return None

    def delete_middle(self):
        if self.get_middle() is not None:
            print("Deleting middle element.")

            # delete that node from the linkedlist
            self.elements.delete_node(self.elements.middle, count=self.top_count + 1)

            # reduce the node count in the stack
            self.top_count -= 1
            return

        print("Stack underflow! Can't delete middle.")
        return None

    def peek(self):
        if self.top_count > -1:
            print(f"Top element {self.elements.head.data}")
            return self.elements.head.data

        print("Stack underflow! No peek.")
        return None

    def peek_all(self):
        if self.top_count > -1:
            print("\nAll elements in stack:")
            self.elements.print_list()
            return

        print("Stack underflow! No peek.")
        return None


if __name__ == "__main__":
    mstack = MiddleStack(5)
    mstack.push(4)
    mstack.push(3)
    mstack.push(2)
    mstack.push(1)
    mstack.push(0)

    mstack.peek()
    mstack.peek_all()

    mstack.get_middle()

    mstack.delete_middle()
    mstack.peek_all()
    mstack.get_middle()

    mstack.pop()

    mstack.get_middle()
    mstack.pop()

    mstack.get_middle()

    mstack.peek_all()

    mstack.pop()

    mstack.get_middle()
    mstack.pop()

    mstack.pop()
    mstack.get_middle()
    mstack.peek_all()
