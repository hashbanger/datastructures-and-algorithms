class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, new_data):
        # creating new node
        new_node = Node(new_data)

        # creating connections
        new_node.next = self.head

        # if head is not none
        if self.head != None:
            self.head.prev = new_node

        # changing the head
        self.head = new_node

    def insert_at_end(self, new_data):
        # creating new node
        new_node = Node(new_data)

        # if head is not None
        if self.head is None:
            self.head = new_node
            return

        # iterating the last node
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next

        ptr.next = new_node
        new_node.prev = ptr

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        new_node = Node(new_data)
        ptr = self.head
        while ptr != None:

            # adding connections with new node
            if ptr.data == prev_node:
                new_node.next = ptr.next
                ptr.next = new_node

                # changing the previous of the next node
                if new_node.next != None:
                    new_node.next.prev = new_node
                break

            ptr = ptr.next

    def insert_before(self, next_node, new_data):
        if next_node is None:
            print("the given next node cannot be NULL")
            return

        new_node = Node(new_data)
        ptr = self.head
        if ptr.data == next_node:
            new_node.next = ptr
            ptr.prev = new_node
            self.head = new_node
            return

        while (ptr != None) and (ptr.next != None):
            if ptr.next.data == next_node:
                new_node.next = ptr.next
                ptr.next = new_node

                ptr.next.prev = new_node
                new_node.prev = ptr
                break

            ptr = ptr.next

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" - ")
            ptr = ptr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.insert_at_end(6)
    llist.insert_at_end(8)
    llist.insert_after(4, 5)
    llist.insert_after(6, 7)
    llist.insert_after(8, 9)
    llist.insert_at_end(11)
    llist.insert_at_end(15)
    llist.insert_at_end(20)
    llist.insert_before(15, 12)
    llist.insert_before(2, 1)
    llist.insert_before(18, 17)
    llist.print_list()
