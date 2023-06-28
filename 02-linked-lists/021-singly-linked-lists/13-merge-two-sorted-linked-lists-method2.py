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


# In place merge of two sorted linked lists
def merge_linked_lists(head_a, head_b):

    # if any of the list is null return the other
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a

    # set the head to whichever head is lower
    if head_a.data > head_b.data:
        temp = head_a
        head_a = head_b
        head_b = temp

    # since the lowest one would be the returning head
    # and head_a is ensured to be lowest, so we store it already.
    result = head_a

    # we keep moving until we run out of both
    while (head_a != None) and (head_b != None):
        ptr = None

        # we keep moving until we find lower values
        # else we switch the heads and connect the ptr to the next lower
        while (head_a != None) and (head_a.data <= head_b.data):
            ptr = head_a
            head_a = head_a.next
        ptr.next = head_b

        # swapping the heads
        temp = head_a
        head_a = head_b
        head_b = temp

    return result


if __name__ == "__main__":
    llist_a = LinkedList()
    llist_a.insert_at_front(15)
    llist_a.insert_at_front(10)
    llist_a.insert_at_front(5)
    llist_a.insert_at_front(1)

    llist_b = LinkedList()
    llist_b.insert_at_front(21)
    llist_b.insert_at_front(20)
    llist_b.insert_at_front(3)
    llist_b.insert_at_front(2)

    merged_list = LinkedList()
    merged_list.head = merge_linked_lists(llist_a.head, llist_b.head)
    merged_list.print_list()
