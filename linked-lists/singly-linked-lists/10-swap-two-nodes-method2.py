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

    # TIME COMPLEXITY: O(N) as we are doing serach for x and y
    # SPACE COMPLEXITY: O(1)
    def swap_nodes(self, x, y):
        if x == y:
            return

        head_ref = self.head
        prev_x = None
        prev_y = None

        # search for previous x and previous y in the list and store their pointers
        while head_ref.next != None:
            if head_ref.next.data == x:
                prev_x = head_ref
            elif head_ref.next.data == y:
                prev_y = head_ref

            head_ref = head_ref.next

        # if x is head of the list
        if prev_x == None and self.head.data == x:
            head_x = self.head
            self.head = prev_y.next
            temp = prev_y.next.next
            prev_y.next.next = head_x.next
            head_x.next = temp
            prev_y.next = head_x
            return
        # if y is head of the list
        elif prev_y == None and self.head.data == y:
            head_y = self.head
            self.head = prev_x.next
            temp = prev_x.next.next
            prev_x.next.next = head_y.next
            head_y.next = temp
            prev_x.next = head_y
            return
        # if neither are the head
        else:
            # if we have both nodes,
            # swap next of current (next of target's previous node)
            temp = prev_x.next
            prev_x.next = prev_y.next
            prev_y.next = temp
            # swapping and next of next (next of target node)
            temp = prev_x.next.next
            prev_x.next.next = prev_y.next.next
            prev_y.next.next = temp

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(6)
    llist.insert_at_front(9)
    llist.insert_at_front(7)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    print("Before Swapping:")
    llist.print_list()
    llist.swap_nodes(6, 1)
    print("\nAfter Swapping:")
    llist.print_list()
