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

# Recursive merge of two sorted linked lists
def merge_linked_lists(head_a, head_b):
    # creating a pointer temp
    temp = None
    # if any of the list is null return the other
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a 
    
    # if head a is smaller add it to pointer
    if head_a.data <= head_b.data:
        temp = head_a
        # recursively merge list 1 ahead of first node and list 2
        # add them to next of temp pointer
        temp.next = merge_linked_lists(head_a.next, head_b)
    else:
        temp = head_b
        temp.next = merge_linked_lists(head_a, head_b.next)

    # return the temp pointer
    return temp


if __name__ == '__main__':
    llist_a = LinkedList()
    llist_a.insert_at_front(15)
    llist_a.insert_at_front(10)
    llist_a.insert_at_front(5)
    llist_a.insert_at_front(4)

    llist_b = LinkedList()
    llist_b.insert_at_front(29)
    llist_b.insert_at_front(20)
    llist_b.insert_at_front(3)
    llist_b.insert_at_front(2)

    merged_list = LinkedList()
    merged_list.head = merge_linked_lists(llist_a.head, llist_b.head)
    merged_list.print_list()