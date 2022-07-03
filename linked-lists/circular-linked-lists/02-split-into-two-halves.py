class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_empty(self, new_data):
        # if not empty return the head
        if self.head != None:
            return self.head
        
        # creating a new node
        new_node = Node(new_data)

        # creating connection
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node

        return self.head
    
    def insert_at_front(self, new_data):
        if self.head == None:
            return self.insert_in_empty(new_data)

        # creating and connecting
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = new_node

    def find_middle(self):
        if self.head is None:
            return None

        slow_ptr = self.head
        fast_ptr = self.head

        while (fast_ptr.next != self.head) and (fast_ptr.next.next != self.head):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr, fast_ptr

    def split_into_two(self, llist1, llist2):
        slow_ptr, fast_ptr = self.find_middle()
        middle = slow_ptr

        ptr = self.head
        while (ptr != middle.next):
            ptr = ptr.next
        
        # if the list is even move the fast ptr to the last node
        if fast_ptr.next.next == self.head:
            fast_ptr = fast_ptr.next

        llist1.head = self.head
        llist2.head = ptr
        llist1.tail = middle
        llist2.tail = fast_ptr

        middle.next = llist1.head
        fast_ptr.next = llist2.head

    def print_list(self):
        if self.head is None:
            print("Empty List")
            return None

        ptr = self.head
        while True:
            print(ptr.data, end = ' - ')
            if ptr.next == self.head:
                print()
                break
            ptr = ptr.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_front(7)
    llist.insert_at_front(6)
    llist.insert_at_front(5)
    llist.insert_at_front(4)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    llist.insert_at_front(1)
    llist.insert_at_front(0)
    # traversing the list
    print("First Linked List")
    llist.print_list()

    llist1 = LinkedList()
    llist2 = LinkedList()
    llist.split_into_two(llist1, llist2)
    print("\nSplit Linked Lists")
    llist1.print_list()
    llist2.print_list()