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

    def rotation_by_k(self, k):
        if k == 0:
            return

        # we use the head as one pointer and another tail pointer
        # then just change the association till the count

        # clockwise rotation
        end_ptr = self.head

        # get a pointer to end
        while end_ptr.next != None:
            end_ptr = end_ptr.next

        # break and add current node to the end
        for _ in range(k):
            current = self.head
            self.head = self.head.next
            current.next = None
            end_ptr.next = current
            end_ptr = end_ptr.next

        return self.head


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

    k = 4
    print(f"Before Rotation by {k}: ")
    llist.print_list()
    llist.head = llist.rotation_by_k(k)
    print(f"\nAfter Rotation by {k}: ")
    llist.print_list()
