# Merging two sorted linked lists
# First we take a dummy node to join everything to, eventually we will return its next as the head of combined list.
# We also have to take a pointer that would move at each step to add the next node from the lists.
# Initially we test if any of the two doesn't exist, if yes then we would just join the existing one to the tail and be done,
# othwerwise we would compare the smaller head, add its node and move its head ahead to next and do this until we have traversed both.
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


# merging two sorted linked lists
def merge_linked_lists(head_a, head_b):
    dummy_node = Node(None)
    ptr = dummy_node
    while True:
        # if a doesn't exist or is exhausted
        if head_a is None:
            ptr.next = head_b
            break

        # if b doesn't exist of is exhausted
        if head_b is None:
            ptr.next = head_a
            break

        # if both are present then
        if head_a.data < head_b.data:
            ptr.next = head_a
            head_a = head_a.next
        else:
            ptr.next = head_b
            head_b = head_b.next

        # move the tail pointer
        ptr = ptr.next

    # return the node next to head
    return dummy_node.next


if __name__ == "__main__":
    llist_a = LinkedList()
    llist_a.insert_at_front(15)
    llist_a.insert_at_front(10)
    llist_a.insert_at_front(5)

    llist_b = LinkedList()
    llist_b.insert_at_front(25)
    llist_b.insert_at_front(20)
    llist_b.insert_at_front(3)
    llist_b.insert_at_front(2)

    merged_list = LinkedList()
    merged_list.head = merge_linked_lists(llist_a.head, llist_b.head)
    merged_list.print_list()
