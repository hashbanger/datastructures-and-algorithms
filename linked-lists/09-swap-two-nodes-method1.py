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
        
        # searching for x (keeping track of previous and current)
        previous_x = None
        current_x = self.head
        while current_x != None and current_x.data != x:
            previous_x = current_x
            current_x = current_x.next

        # searching for y (keeping track of previous and current)
        previous_y = None
        current_y = self.head
        while current_y != None and current_y.data != y:
            previous_y = current_y
            current_y = current_y.next

        # if either of them is not found then return
        if current_x == None or current_y == None:
            return

        # if x is not the head of the list
        if previous_x != None:
            previous_x.next = current_y
        else:
            self.head = current_y

        # if y is not the head of the list
        if previous_y != None:
            previous_y.next = current_x
        else:
            self.head = current_x
        
        # swapping the next pointers
        temp = current_x.next
        current_x.next = current_y.next
        current_y.next = temp

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

if __name__ == '__main__':
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
    llist.swap_nodes(1, 6)
    print("\nAfter Swapping:")
    llist.print_list()