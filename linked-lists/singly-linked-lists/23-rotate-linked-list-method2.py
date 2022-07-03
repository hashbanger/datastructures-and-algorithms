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

        # clockwise rotation
        current = self.head

        counter = 1
        # moving to kth node
        while counter < k and current != None:
            current = current.next
            counter += 1

        # keeping a pointer at kth, right before the new head
        kth_node = current

        # move the current node to the end
        while current.next != None:
            current = current.next

        # then join it to head
        current.next = self.head

        # change the head
        self.head = kth_node.next

        # break the connection before new head
        kth_node.next = None

        return self.head


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(60)
    llist.insert_at_front(50)
    llist.insert_at_front(40)
    llist.insert_at_front(30)
    llist.insert_at_front(20)
    llist.insert_at_front(10)
    k = 4
    print(f"Before Rotation by {k}: ")
    llist.print_list()
    llist.head = llist.rotation_by_k(k)
    print(f"\nAfter Rotation by {k}: ")
    llist.print_list()
