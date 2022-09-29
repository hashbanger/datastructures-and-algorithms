class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next

    def detect_and_remove_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head

        # we will iterate the list with slow and fast pointers
        # if the meet each other would mean there's a loop somewhere.
        while (slow_ptr != None) and (fast_ptr != None) and (fast_ptr.next != None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            # if they are on the same node then there's a loop
            if slow_ptr.data == fast_ptr.data:

                # removing the loop
                self.remove_loop(slow_ptr)
                return

    def remove_loop(self, slow_ptr):
        # first we count the number of nodes in the loop
        count = 1
        ptr = self.head
        while ptr.next != slow_ptr:
            count += 1
            ptr = ptr.next

        # set pointer 1 to head and pointer 2 to count (N) nodes ahead of head
        ptr1 = self.head
        ptr2 = self.head
        for _ in range(count):
            ptr2 = ptr2.next

        # Now we keep moving until they are equal, so we reach the repeated node
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Now we circle back the second pointer to the previous of repeated node
        # then disconnect it from the loop
        while ptr2.next != ptr1:
            ptr2 = ptr2.next
        ptr2.next = None


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(11)
    llist.insert_at_front(10)
    llist.insert_at_front(9)
    llist.insert_at_front(8)
    llist.insert_at_front(7)
    llist.insert_at_front(6)
    llist.insert_at_front(5)
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    llist.head.next.next.next.next.next.next.next.next.next.next.next = (
        llist.head.next.next
    )

    print(llist.head.data, end=" - ")
    print(llist.head.next.data, end=" - ")
    print(llist.head.next.next.data, end=" - ")
    print(llist.head.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.next.next.data, end=" - ")
    print(llist.head.next.next.next.next.next.next.next.next.next.next.next.data)

    llist.detect_and_remove_loop()
    llist.print_list()
